n =1
lista =[]

while n != 0:
    n = int(input())
    for i in range(1, n + 1):
        lista.append(i)
        lista[i-1] = str(lista[i-1])
        i = i + i
    lista=' '.join(lista)
    if n!= 0:      
        print(lista)
        lista =[]