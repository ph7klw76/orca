
import re
import math
import os
def calculate_spin_orbit_coupling(filename):
    # Store the total spin-orbit coupling for each Root
    total_soc_by_root = {}
    f=open(filename, 'r')
    ii=-1000000
    for i,line in enumerate(f):
        if "CALCULATED SOCME BETWEEN TRIPLETS AND SINGLETS " in line:
            ii=i+5
        if ii<=i<=ii+110:
            values =re.split(r'\s+', line.strip())
            values= [x for x in values if x not in [',', '(', ')']]
            if len(values)>=7:
                root0 = values[0]  # Root (T)
                root1 = values[1]  # Root (T)
                # Extract complex numbers for Z, X, and Y
                z = complex(float(values[2]), float(values[3]))
                x = complex(float(values[4]), float(values[5]))
                y = complex(float(values[6]), float(values[7]))
                # Calculate the total spin-orbit coupling for this line
                total_soc = math.sqrt(abs(z)**2 + abs(x)**2 + abs(y)**2)             
                # Update the total spin-orbit coupling for this root
                total_soc_by_root[root0,root1] = total_soc_by_root.get(root0, 0) + total_soc
    return total_soc_by_root
if __name__ == "__main__":
    base_path = "D:/LS19/"
    output_filename = "spin_orbit_couplings.txt"
    root_sums = {}  # Sum of SOC for each root
    root_values = {}  # List of SOC values for each root
    root_counts = {}  # Count of occurrences for each root

    with open(output_filename, 'w') as output_file:
        for x in range(1, 26):  # x varies from 1 to 25
            filename = os.path.join(base_path, f"molecule_{x}.out")
            if os.path.exists(filename):
                total_soc_by_root = calculate_spin_orbit_coupling(filename)
                output_file.write(f"Total Spin-Orbit Coupling for Molecule {x} by Root:\n")
                
                for root, total_soc in total_soc_by_root.items():
                    output_file.write(f"Root {root}: {total_soc} cm-1\n")
                    root_sums[root] = root_sums.get(root, 0) + total_soc
                    root_counts[root] = root_counts.get(root, 0) + 1
                    if root not in root_values:
                        root_values[root] = []
                    root_values[root].append(total_soc)
            else:
                output_file.write(f"File {filename} does not exist. Skipping.\n")
        
        # Calculate and write the averages
        output_file.write("\nAverage Spin-Orbit Coupling by Root:\n")
        for root in root_sums.keys():
            average = root_sums[root] / root_counts[root]
            output_file.write(f"Average for Root {root}: {average} cm-1\n")
        
        # Calculate and write the standard deviations
        output_file.write("\nStandard Deviation of Spin-Orbit Coupling by Root:\n")
        for root, values in root_values.items():
            average = root_sums[root] / root_counts[root]
            variance = sum((x - average) ** 2 for x in values) / root_counts[root]
            std_dev = math.sqrt(variance)
            output_file.write(f"Standard Deviation for Root {root}: {std_dev} cm-1\n")
