lista = []
for x in range(0,10):
    n = input()
    lista.append(int(n))

pos = max(lista)

print(max(lista))
print(lista.index(pos) + 1)