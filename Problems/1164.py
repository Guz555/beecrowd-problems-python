n = input()

for x in range(0, int(n)):
    n1 = input()
    lista = [x for x in range(1, int(n1)) if int(n1) % x == 0]
    if sum(lista) == int(n1):
        print(f'{n1} eh perfeito')
    else:
        print(f'{n1} nao eh perfeito')