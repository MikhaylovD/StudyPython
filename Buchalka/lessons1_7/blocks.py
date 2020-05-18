# for i in range(1, 13):
#     print(("no. {} squared is {} and cubed is {:4}".format(i,  i ** 2, i ** 3)))
# print("*" * 80)

name = input("Please enter Name")
age = int(input("How ols are you, {0}?".format(name)))
print(age)

if age >= 18:
        print("You are old enough")
else:
    print("Please come back in {0}".format(18-age))
