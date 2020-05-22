def python_food():
    print("spam and eggs")


def centre_text(*args, sep='', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text +=str(arg) + sep
    return text, "3"


# with open("centred", mode='w') as centred_file:
#     centre_text("first line", file=centred_file)
#     centre_text("first", "second", 3, 4, file=centred_file)


print(centre_text("first line"))
print(centre_text("first", "second", 3, 4, sep=":"))