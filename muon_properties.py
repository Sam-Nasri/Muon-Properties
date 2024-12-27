import os

# File Paths
muons_file = os.path.join('muons.txt')
muon_properties = os.path.join('muon_properties.txt')

readfile = open(muons_file, "r")
read_data = readfile.readlines()

with open(muons_file, "r") as readfile:
    read_data = readfile.readlines()

with open(muon_properties, "w") as writefile:
    for line in read_data:
        if 'Njets' in line:
            writefile.write(line)
