
""" calculate reorganization between S1 and T1"""

import os
import pandas as pd

def extract_last_e_tot_value(file_path):
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

def process_directory_and_update_excel(filename, excel_path ,Reorganization_Energy):
    filename=filename.split('.out')[0]
    df = pd.read_excel(excel_path) # Load the Excel file
    # Ensure there's a column for the update, adding one if necessary
    if 'Reorganization_Energy' not in df.columns:
        df['Reorganization_Energy'] = None  # Initialize a new column with None values
    # Update the dataset with the specified value if the search_filename is found
    if filename in df['Filename'].values:
        # Find the index and update the value
        df.loc[df['Filename'] ==filename , 'Next Column'] = Reorganization_Energy
        update_status = "Value updated successfully."
    else:
        update_status = "Filename '{}' not found in the dataset.".format(filename)
    update=excel_path.split('.xlsx')[0]+'_updated.xlsx'
    df.to_excel(update, index=False)
    return update_status 

directory_path="D:/labkicosmos/1/round2"
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path) and file_path.endswith('.out'):
        e_tot_value = extract_last_e_tot_value(file_path)
        if e_tot_value is not None:
            pass
        else:
            print("No E(tot) value found between 'JOB NUMBER 1' and 'OPTIMIZATION RUN DONE'.")
        last_e_tot_value2 = extract_last_e_tot_value_global(file_path)
        if last_e_tot_value2 is not None:
            pass
        else:
            print("No 'E(tot)  =' value found in the file.")
        E1=float(e_tot_value)
        E2=float(last_e_tot_value2)
        Reorganization_Energy=E2-E1
        print(filename,Reorganization_Energy) #reorganization energy
        excel_path = 'D:/labkicosmos/Book2.xlsx'  # Adjust the path to your Excel file
        process_directory_and_update_excel(filename, excel_path ,Reorganization_Energy)
