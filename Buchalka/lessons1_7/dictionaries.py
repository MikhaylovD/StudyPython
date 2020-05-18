fruit = {"orange": "a sweet",
         "apple": "good for cider",
         "lemon": "yellow",
         "lime": "a sour, green"}
# print(fruit)
# print(fruit["apple"])
# fruit["pear"] = "an old shaped apple"
# print(fruit["pear"])
# del fruit["lemon"]
# fruit.clear()
print(fruit)
# while True:
    # dict_key = input("enter a fruit: ")
    # if dict_key == "quit":
    #     break
    # description = fruit.get(dict_key, "we dont have a " + dict_key)
    # print(description)
    # # if dict_key in fruit:
    # #     description = fruit.get(dict_key)
    # #     print(description)
    # # else:
    # #     print("we dont have a " + dict_key)

# for snack in fruit:
#     print(fruit[snack])

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + "--" + fruit[f])

print(fruit.items())
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, descrip = snack
    print(item + " " + descrip)