lista = []

for x in range(0, 20):
    n = int(input())
    lista.append(n)

contador = 0
for x in lista[::-1]:
    print(f'N[{contador}] = {x}')
    contador += 1
