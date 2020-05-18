shoppin_list = ["milk", "pasta", "eggs", "bread", "spam"]

# for item in shoppin_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

item_to_find = "spam"
found_at = None

# for index in range(len(shoppin_list)):
#     if shoppin_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shoppin_list:
    found_at = shoppin_list.index(item_to_find)
if found_at is not None:
    print("Item found {} ".format(found_at))
else:
    print("{} not found".format(item_to_find))