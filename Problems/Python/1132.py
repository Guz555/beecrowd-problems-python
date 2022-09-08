n1 = input()
n2 = input()
lista = []
if int(n1) < int(n2):
    for x in range(int(n1), int(n2)+1):
        if x % 13 != 0:
            lista.append(x)
else:
    for x in range(int(n2), int(n1)+1):
        if x % 13 != 0:
            lista.append(x)

print(sum(lista))