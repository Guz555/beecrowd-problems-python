c, n = input().split()
lista = [x for x in range(1, int(n)+1)]
n = 0
for i in range(0, int(c)):
    n += 1
    if n > len(lista) - 1:
        n = 0
print(n)

"""x, y = input().split()
x = int(x)
y = int(y)

if x > y:
    print(x % y)
else:
    print(y % x)"""
