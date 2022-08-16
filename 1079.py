num = input()
lista = []
for x in range(0, int(num)):
    linha = input().split()
    n1, n2, n3 = linha
    media = ((float(n1) * 2) + (float(n2) * 3) + (float(n3) * 5)) / (2 + 3 + 5)
    lista.append(media)

for x in lista:
    print(f'{x:.1f}')