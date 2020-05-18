# my_list = list(range(10))
#
# print(my_list)
#
# my_string = "abcdef"
# print((my_string.index('e')))
# print(my_string[4])
#
# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
#
# print(range(0, 100)[::-2] == range(99, 0, -2))
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)