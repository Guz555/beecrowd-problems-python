x = -1
lista2 = []

while int(x) != 0:
    x = input()
    lista = []
    if int(x) == 0:
        continue
    
    for i in range(0, 5):
        if int(x) % 2 != 0:
            x = int(x) + 1
        lista.append(int(x))
        x = int(x) + 1
    lista2.append(sum(lista))

for x in lista2:
    print(x)