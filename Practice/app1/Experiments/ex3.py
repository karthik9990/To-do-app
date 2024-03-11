textfiles = ["a.txt", "b.txt", "c.txt"]

for filename in textfiles:
    file = open(filename, 'r')
    content = file.read()
    print(content)