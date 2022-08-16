n1 = input()
n2 = input()
lista = []

if int(n1) < int(n2):
    while int(n1) <= int(n2):
        n1 = int(n1) + 1
        if int(n1) == int(n2):
            break
        lista.append(n1)

elif int(n1) > int(n2):
    while int(n2) <= int(n1):
        n2 = int(n2) + 1
        if int(n1) == int(n2):
            break
        lista.append(n2)
    
lista2 = [(x) for x in lista if x % 2 != 0]

if not lista2:
    print(0)
else:
    print(sum(lista2))