import shelve

fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, or"
# fruit['apple'] = "a sweet, apple"
# fruit['lemon'] = "a sweet, lemon"
# fruit['grape'] = "a sweet, grape"
# fruit['lime'] = "a sweet, liome"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit['lime'] = "greate with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     shelf_key = input("enter fruit")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "we don't nave this")
#     print(description)

ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " - " + fruit[f])
fruit.close()
