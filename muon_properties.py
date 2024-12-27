import os

muons_file = os.path.join('muons.txt')

readfile = open(muons_file, "r")
read_data = readfile.readlines()

# Use context manager to automatically handle closing the file
with open(muons_file, "r") as readfile:
    read_data = readfile.readlines()

# print(len(data))  # To get the number of lines in the txt file and for us to make sure we read the file correctly

for line in read_data:
    print(line)
