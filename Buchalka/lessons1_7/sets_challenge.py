string = input("write something")

vowels = frozenset("aeioyu")
set_no_vowels = set(string).difference(vowels)


print(sorted(set_no_vowels))