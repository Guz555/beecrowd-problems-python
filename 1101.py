linha = input().split()
m, n = linha
lista = []
while int(m) > 0 and int(n) > 0:
    if int(m) > int(n):
        lista2 = []
        for x in range(int(n), int(m) + 1):
            lista2.append(x)
    elif  int(n) > int(m):
        lista2 = []
        for x in range(int(m), int(n) + 1):
             lista2.append(x)

    lista.append(lista2)


    linha = input().split()
    m, n = linha

for x in lista:
    a = sum(x)
    for y in x:
        print(y, end= ' ')
    print(f'Sum={a}')