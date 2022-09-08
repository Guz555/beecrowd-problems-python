n = input()
lista2 = []
for i in range(0, int(n)):
    lista = []
    x, y = input().split()
    for j in range(0, int(y)):
        if int(x) % 2 == 0:
            x = int(x) + 1
        lista.append(int(x))
        x = int(x) + 1
    lista2.append(sum(lista))

for x in lista2:
    print(x)