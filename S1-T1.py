def extract_last_e_tot_value(file_path):
    """
    Extracts the last E(tot) value between "JOB NUMBER 1" and "OPTIMIZATION RUN DONE".
    
    Parameters:
    file_path (str): The path to the file to be read.
    
    Returns:
    float: The extracted E(tot) value.
    """
    with open(file_path, 'r') as file:
        content = file.readlines()

    job_start = False
    e_tot_values = []

    for line in content:
        if "JOB NUMBER  1" in line:
            job_start = True
        elif "OPTIMIZATION RUN DONE" in line:
            break  # Stop reading further as we've reached the end of the relevant section
        elif job_start and "E(tot)  =" in line:
            e_tot_values.append(line)

    # Extracting the floating point number from the last occurrence of "E(tot)  ="
    if e_tot_values:
        last_e_tot_line = e_tot_values[-1]
        last_e_tot_value_str = last_e_tot_line.split('=')[-1].strip().split()[0]  # Splitting and taking the first part
        last_e_tot_value = float(last_e_tot_value_str)
        return last_e_tot_value
    else:
        return None

def extract_last_e_tot_value_global(file_path):
    """
    Extracts the very last E(tot) value from the file.
    
    Parameters:
    file_path (str): The path to the file to be read.
    
    Returns:
    float: The extracted E(tot) value, or None if not found.
    """
    with open(file_path, 'r') as file:
        content = file.readlines()

    e_tot_values = []

    for line in content:
        if "E(tot)  =" in line:
            e_tot_values.append(line)

    # Extracting the floating point number from the very last occurrence of "E(tot)  ="
    if e_tot_values:
        last_e_tot_line = e_tot_values[-1]
        last_e_tot_value_str = last_e_tot_line.split('=')[-1].strip().split()[0]  # Splitting and taking the first part
        last_e_tot_value2 = float(last_e_tot_value_str)
        return last_e_tot_value2
    else:
        return None
# Example usage
if __name__ == "__main__":
    file_path = './12-3-Se.out'  # Adjust the path to where your file is located
    e_tot_value = extract_last_e_tot_value(file_path)
    if e_tot_value is not None:
        print(f"The last E(tot) value is: {e_tot_value}")
    else:
        print("No E(tot) value found between 'JOB NUMBER 1' and 'OPTIMIZATION RUN DONE'.")
    last_e_tot_value2 = extract_last_e_tot_value_global(file_path)
    if last_e_tot_value2 is not None:
        print(f"The very last E(tot) value in the file is: {last_e_tot_value2}")
    else:
        print("No 'E(tot)  =' value found in the file.")
E1=float(e_tot_value)
E2=float(last_e_tot_value2)
g=E2-E1
print("reorganization energy:",g)
