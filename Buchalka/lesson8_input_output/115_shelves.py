import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, or"
    fruit['apple'] = "a sweet, apple"
    fruit['lemon'] = "a sweet, lemon"
    fruit['grape'] = "a sweet, grape"
    fruit['lime'] = "a sweet, liome"

    print(fruit["lemon"])
    print(fruit["grape"])