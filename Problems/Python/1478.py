"""
  1   2   3   4   5
  2   1   2   3   4
  3   2   1   2   3
  4   3   2   1   2
  5   4   3   2   1
"""

lista = []
n = int(input())
for x in range(n):
    lista.append([x+1])
    l = 0
    for y in range(n):
        l += 1
        lista[x].append(l)

print(lista)
