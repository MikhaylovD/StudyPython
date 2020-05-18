name = input(" - Enter name: ") ### NAME check
while name == "":
    print("No NAME provided. Try again.")
#name = input(" - Enter name: ")

age = "" ### AGE check ###
checkString = "0123456789"
notCorrectAge = True;

while notCorrectAge:

    age = input(" - Enter age: ") ### AGE check ###

    for character in age:
        if character not in checkString or age == "":
            print("No AGE provided. Try again.")
            break
        notCorrectAge = False

if age == "": ### AGE to int
    age = 0
else:
    age = int(age)

print(age)

if age != 0 and (18 < age < 30): ### Final
    print("Welcome, {}!!!".format(name))
else:
    print("You are not meeting our requirements, {}. \nHave a good day.".format(name))