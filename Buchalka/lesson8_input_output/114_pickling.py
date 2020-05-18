import pickle
#
# imelda = ('More Mayhem',
#           'Imelada May',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayham')))
#
# with open("114_imelda.pickle",'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("114_imelda.pickle",'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#     print(imelda2)

imelda = ('More Mayhem',
          'Imelada May',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayham')))

even = list(range(0, 10, 2))
with open("114_imelda.pickle",'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(777, pickle_file, protocol=0)

with open("114_imelda.pickle",'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even2 = pickle.load(imelda_pickled)
    number2 = pickle.load(imelda_pickled)
    print(imelda2)
    print(even2)
    print(number2)