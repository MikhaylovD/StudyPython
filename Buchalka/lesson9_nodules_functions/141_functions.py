def python_food():
    print("spam and eggs")


def centre_text(*args, sep='', end='\n', file=None, flush=False):
    text = "";
    for arg in args:
        text +=str(arg) + sep
    print(text, end=end, file=file, flush=flush)

python_food()
centre_text("first", "second", 3, 4, sep=":")
