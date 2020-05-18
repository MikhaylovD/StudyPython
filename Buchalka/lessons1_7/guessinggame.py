import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: remove after test
guess = 0
print("Please guess number 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

# if guess != answer:
#     if guess <answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Sorry, you have not guessed")
# else:
#     print("You got it")

