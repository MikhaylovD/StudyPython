inputFile = "original.txt"

myFile = open(inputFile, 'r', encoding='utf-8')
# print(myFile.read())

for line in myFile:
    print(line.strip())