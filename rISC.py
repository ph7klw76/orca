import numpy as np


#S1 to T1
# Constants
hbar = 6.582E-16  # Planck's constant, eV
kB = 8.6173303E-5  # Boltzmann's constant, eV K^-1

# Given values
V_cm1 = 0.127279221       # Frequency factor in cm^-1
deltaEst_eV = 0.12449138  # Energy barrier in eV
lambda_eV = 0.427404161   # Reorganization energy in eV
T = 300                   # Temperature in K

# Convert V from cm^-1 to eV
V_eV =1.2398E-6*V_cm1

# Calculate the rate constant k
k = (2 * np.pi * V_eV**2) / (hbar)
k_rsc=k*np.exp((-1*(lambda_eV+deltaEst_eV)**2)/(4*lambda_eV*kB*T))
k_rsc=k_rsc/(3*np.sqrt(4*np.pi*kB*T*lambda_eV))
k_isc=k*np.exp((-1*(lambda_eV-deltaEst_eV)**2)/(4*lambda_eV*kB*T))
k_isc=k_isc/(np.sqrt(4*np.pi*kB*T*lambda_eV))
print(f"The rate constant k_rsc is: {k_rsc} s^-1")
print(f"The rate constant k_isc is: {k_isc} s^-1")


# T2 to S1
# Given values
V_cm1 = 1.107971119       # Frequency factor in cm^-1
T2= 3.45281886  # Energy barrier in eV
S1= 3.00593862
deltaEst_eV= S1-T2  #negative
lambda_eV = 0.427404161   # Reorganization energy in eV
T = 300                   # Temperature in K

# Convert V from cm^-1 to eV
V_eV =1.2398E-6*V_cm1

# Calculate the rate constant k
k_rsc=k*np.exp((-1*(lambda_eV+deltaEst_eV)**2)/(4*lambda_eV*kB*T))
k_rsc=k_rsc/(3*np.sqrt(4*np.pi*kB*T*lambda_eV))
k_isc=k*np.exp((-1*(lambda_eV-deltaEst_eV)**2)/(4*lambda_eV*kB*T))
k_isc=k_isc/(np.sqrt(4*np.pi*kB*T*lambda_eV))
print(f"The rate constant k_rsc T2 to S1 is: {k_rsc} s^-1")
print(f"The rate constant k_isc S1 to T2 is: {k_isc} s^-1")
