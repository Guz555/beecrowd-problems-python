linha = input().split()
lista = []

for x in linha:
    lista.append(x)

a = lista[0]
n = lista[len(lista) -1]
lista2 = []
i = 0
while i < int(n):  
    lista2.append(i + int(a))
    i += 1

print(sum(lista2))
