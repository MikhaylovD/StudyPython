n = 10

A = [x ** 2 for x in range(n)]
B = [x ** 2 for x in range(n) if x % 2 == 0]

print(A)
print(B)

cities = ["Moscow", "Tver"]
C = [city for city in cities if len(city) < 5]
print(C)

# //////////////////////////////////////////

x = int(input("enter digit"))
digs = []
while x:
    digs.append(x % 10)
    x = x // 10
digs.reverse()
print(digs)

# //////////////////////////////////////////

N = 11
A = list(range(N))
print(A)

for i in range(N // 2):
    A[i], A[N - i - 1] = A[N - i - 1], A[i]
print(A)

# //////////////////////////////////////////

