l = []
n = int(input())
cont = 0
print(f'N[{cont}] = {n}')
for x in range(0,9):
    cont += 1
    n = n * 2
    print(f'N[{cont}] = {n}')
    