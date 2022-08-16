x, y = input().split()
contador = 0

lis = []
lista = []

teste = None
for i in range(1, int(y)+ 1):
    lis.append(i)

for a in range(0, len(lis)):
    if contador > len(lis) -1:
        break
    for b in range(0,int(x)):
        if contador > len(lis)-1:
            break
        lista.append(str(lis[contador]))
        contador += 1
    teste = ' '.join(lista)
    print(teste)
    lista = []
