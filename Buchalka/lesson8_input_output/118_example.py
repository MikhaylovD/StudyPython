import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "tomato", "bread"],
                    "beans_on_toast": ["bean", "bread"],
                    "scrambles_eggs": ["eggs", "butter"],
                    "soup": ["tin of soup", "water"],
                    "paste": ["pasta", "cheese"]},
books["maintenance"] = {"stuck": ["oil"],
                    "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["scrambles_eggs"])
# print(books["maintenance"]["loose"])
books.close()