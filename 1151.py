n = input()
n2 = 1
n3 = 1
lista = ['0', '1', '1']
lista2 = []
a = 2
for x in range(0, int(n)-3):
    a = n2 + n3
    n3 = n2
    n2 = a
    lista.append(str(a))

lista = ' '.join(lista)

print(lista)
