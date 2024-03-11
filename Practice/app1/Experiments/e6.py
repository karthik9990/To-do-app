# using glob module


import glob

myfile = glob.glob("*.txt")
for filepath in myfile:
    with open(filepath, 'r') as file:
        print(file.read().upper())
