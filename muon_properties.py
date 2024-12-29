import os
import re

# File Paths
muons_file = os.path.join('muons.txt')
muon_properties = os.path.join('muon_properties.txt')

def extract_muon_properties(line):
    # Capturing the values of pt, eta, phi, and m using a regex 
    match = re.search(r"pt,eta,phi,m=\s*([\d.]+)\s*([\d.-]+)\s*([\d.-]+)\s*([\d.]+)", line) 
    if match:
        pt, eta, phi, m = match.groups()    # Unpacking the values from the match.groups() tuple
        return pt, eta, phi, m
    return None

with open(muons_file, "r") as readfile, open(muon_properties, "w") as writefile:
    for line in readfile:
        if 'm1:' in line or 'm2:' in line:  # Looking for lines that contain m1 or m2
            muon_data = extract_muon_properties(line)   # Creating a tuple muon_data that has the same the values as the tuple match.groups()  
            if muon_data:
                pt, eta, phi, m = muon_data # Unpacking the values from the muon_data tuple
                muon_label = "muon1" if 'm1:' in line else "muon2"  # Labeling the muon to distinguish the values between m1 and m2 
                writefile.write(f"{muon_label}: pt={pt}, eta={eta}, phi={phi}, m={m}\n")
