import re
import math

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
                total_soc_by_root[root0,root1] = total_soc_by_root.get(root, 0) + total_soc
    return total_soc_by_root

if __name__ == "__main__":
    filename = "D:/LS19/molecule_25.out"
    total_soc_by_root = calculate_spin_orbit_coupling(filename)
   
    # Print the results
    print("Total Spin-Orbit Coupling by Root:")
    for root, total_soc in total_soc_by_root.items():
        print(f"Root {root}: {total_soc} cm-1")
