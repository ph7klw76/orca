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



# List to hold .out files
out_files = []
base_path = "D:/OSC/file/"
# Walk through the directory
for root, dirs, files in os.walk(base_path):
    for file in files:
        # Check if the file ends with .out
        if file.endswith('.out'):
            # Add the file to the list
            out_files.append(file.split('.')[0])
if __name__ == "__main__":
    for file in out_files:
        output_filename = "spin_orbit_couplings.txt"
        root_sums = {}  # Sum of SOC for each root
        root_values = {}  # List of SOC values for each root
        root_counts = {}  # Count of occurrences for each root
    
        with open(output_filename, 'w') as output_file:
            filename = os.path.join(base_path, f"{file}.out")
            total_soc_by_root = calculate_spin_orbit_coupling(filename)
            output_file.write(f"Total Spin-Orbit Coupling for Molecule {file} by Root:\n")           
            for root, total_soc in total_soc_by_root.items():
                output_file.write(f"Root {root}: {total_soc} cm-1\n")
                root_sums[root] = root_sums.get(root, 0) + total_soc
                root_counts[root] = root_counts.get(root, 0) + 1
                if root not in root_values:
                    root_values[root] = []
                root_values[root].append(total_soc)
    
        # Calculate and write the averages
        output_file.write("\nAverage Spin-Orbit Coupling by Root:\n")
        for root in root_sums.keys():
            average = root_sums[root] / root_counts[root]
            output_file.write(f"Average for Root {root}: {average} cm-1\n")
            print(average)
        # Calculate and write the standard deviations
        output_file.write("\nStandard Deviation of Spin-Orbit Coupling by Root:\n")
        for root, values in root_values.items():
            average = root_sums[root] / root_counts[root]
            variance = sum((x - average) ** 2 for x in values) / root_counts[root]
            std_dev = math.sqrt(variance)
            output_file.write(f"Standard Deviation for Root {root}: {std_dev} cm-1\n")
