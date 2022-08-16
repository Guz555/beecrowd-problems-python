l = []
cont = 0
for x in range(0, 10):
    n = int(input())
    l.append(n)

for x in l:
    if x <= 0:
        x = 1
        print(f'X[{cont}] = {x}')
    else:
        print(f'X[{cont}] = {x}')
    cont += 1