lista = []
qnt = 0
for x in range(1,7):
    n1 = input()
    lista.append(n1)

for x in lista:
    if float(x) > 0:
        qnt += 1

print(f'{qnt} valores positivos')

