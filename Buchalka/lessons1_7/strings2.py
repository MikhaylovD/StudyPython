# parrot = "Blue norwrgian"
# print(parrot)
#
# print(parrot[3])
#
# print(parrot[0:6])

# number = "9,223,372,036 854"
number = input("Please enter something")
separators = "";

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))
