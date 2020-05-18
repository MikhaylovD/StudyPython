a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 23, 45, "forth", -50]

temp_key = ""
d = {}
for element in a:
    if type(element) == str:
        d[element] = []
        temp_key = element
    else:
        d[temp_key].append(element)

for k,v in d.items():
    print(k + ": " + str(v))

my_text = "привет пока привет пока стол Стол Привет да нет"

my_text_list = my_text.split()
dict = {}
for element in my_text_list:
    # if element in dict:
    #     dict[element] += dict[element]
    # else:
    #     dict[element] = 1
    dict[element] = dict.get(element, 0) + 1

print(dict)