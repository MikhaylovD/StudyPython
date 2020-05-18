file = open('original.txt')
print(file.read(3))
print(file.read(3))
file.seek(0)

print(file.read(3))
