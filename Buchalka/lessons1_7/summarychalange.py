choice = "-"

while choice != "0":

    if choice in "12345":
        print("Your chose {}".format(choice))
    else:
        print("chose your option:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn C#")
        print("4:\tHave dinner")
        print("5:\tExit")

    choice = input()