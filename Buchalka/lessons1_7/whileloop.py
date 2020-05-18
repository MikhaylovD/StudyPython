# for i in range (10):
#     print("i is now {} ".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

availabl_exiats = ["north", "south", "east"]
choden_exit = ""
while choden_exit not in availabl_exiats:
    choden_exit = input("Please choose value")
    if choden_exit.casefold() == "quit":
        print("Game over")
        break

print("OK")