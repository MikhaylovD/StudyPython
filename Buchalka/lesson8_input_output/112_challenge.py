
with open("112_challenge.txt", 'w') as challenge_file:
    for i in range(1, 13):
        print("{0} times 2 is {1}".format(i, i*2), file=challenge_file)
