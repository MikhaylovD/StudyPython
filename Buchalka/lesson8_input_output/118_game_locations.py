import shelve

locations = shelve.open("118_game_locations")
locations["0"] = {"desc": "You are sitting in front of computer",
                  "exits": {},
                  "namedExits": {}}

locations["1"] = {"desc": "You are standing in at the end of",
                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}}

locations["2"] = {"desc": "You are at the top of a hill",
                  "exits": {"N": 5, "Q": 0},
                  "namedExits": {"5": 5}}

locations["3"] = {"desc": "You are inside a building",
                  "exits": {"W": 1, "Q": 0},
                  "namedExits": {"1": 1}}

locations["4"] = {"desc": "You are in a valley in beside a stream",
                  "exits": {"N": 5, "W": 2, "Q": 0},
                  "namedExits": {"1": 1, "2": 2}}

locations["5"] = {"desc": "You are in the forrest",
                  "exits": {"W": 2, "S": 1, "Q": 0},
                  "namedExits": {"2": 2, "1": 1}}

locations["vocabulary"] = {"QUIT": "Q",
                           "NORTH": "N",
                           "SOUTH": "S",
                           "EAST": "E",
                           "WEST": "W",
                           "ROAD": "1",
                           "HILL": "2",
                           "BUILDING": "3",
                           "VALLEY": "4",
                           "FOREST": "5"}
locations.close()
