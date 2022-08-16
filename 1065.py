lista = []
qnt = 0
for x in range(1,6):
    n1 = input()
    lista.append(n1)

for x in lista:
    if int(x) % 2 == 0:
        qnt += 1

print(f'{qnt} valores pares')

