# print(dir())
#
# for m in dir(__builtins__):
#     print(m)
import shelve
from builtins import print

# print(dir())
# print()
# print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
