n = input()
lista = []

for x in range(0, int(n)):
    n1 = input()
    lista.append(int(n1))

for x in lista:
    if x > 0 and x % 2 == 0:
        print('EVEN POSITIVE')
    elif x > 0 and x % 2 != 0:
        print('ODD POSITIVE')
    elif x < 0 and x % 2 == 0:
        print('EVEN NEGATIVE')
    elif x < 0 and x % 2 != 0:
        print('ODD NEGATIVE')
    if not x:
        print('NULL')
