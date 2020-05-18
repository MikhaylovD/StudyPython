d = {"Alex": 25, "Petr": 15}
d["Kate"] = 19

print(d["Petr"])
d[10] = 20

# print(d)
# проход по словарю
for key, value in d.items():
    print("key: " + str(key) + ", value: " + str(value))
