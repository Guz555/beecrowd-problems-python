n = int(input())
lista = []
for x in range(n+1):
    a = input().split()
    lista.append(a)

l = 0
c = 0
a = []
for x in range(n+1):
    for x in lista[l:c]:
        for y in x[l:c]:
            print(y)
        c+= 1
    l+= 1



"""
# 0  1  2
 [0, 1, 1]
 [0, 1, 1]
 [0, 1, 1]
 [0, 1, 1]
"""
