
n = input()
lista = []
lista2 = []
for x in range(0, int(n)):
    linha = input().split()
    a, b = linha
    if int(a) > int(b):
        while int(a) >= int(b):
            b = int(b) + 1
            if int(b) == int(a):
                lista2.append(sum(lista))
                lista = []
                break
            elif b % 2 != 0:
                lista.append(b)
            
    elif int(b) > int(a):
        while int(b) >= int(a):
            a = int(a) + 1
            if int(a) == int(b):
                lista2.append(sum(lista))
                lista = []
                break
            elif a % 2 != 0:
                lista.append(a)

    elif int(a) == int(b):
        lista2.append(0)

for x in lista2:
    print(x)
    