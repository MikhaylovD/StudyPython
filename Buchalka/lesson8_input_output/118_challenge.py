import shelve

locations = shelve.open("118_game_locations")

loc = "1"
while True:
    availableExits = "".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == "0":
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in locations["vocabulary"]:
                direction = locations["vocabulary"][word]
                break
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]

    if direction in allExits:
        loc = str(allExits[direction])
    else:
        print("You cannot go in that direction")

locations.close()
