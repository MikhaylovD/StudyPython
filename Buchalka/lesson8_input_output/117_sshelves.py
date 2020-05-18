import shelve

blt = ["bacon", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    recipes["soup"].append("water")

    for snack in recipes:
        print(snack, recipes[snack])