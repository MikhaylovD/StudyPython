low = 1
high = 1000
print("Please think between {} and {}".format(low, high))
input("please ENTER ti start")

guesses = 1
while high != low:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower?"
                     "Enter h or l"
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h,l or c")
    guesses = guesses + 1
else:
    print("You thought oh the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
