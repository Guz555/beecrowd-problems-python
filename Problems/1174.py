l = []
cont = 0
for x in range(1,101):
    n = float(input())
    l.append(n)

for x in l:
    if x <= 10:
        print(f'A[{cont}] = {x:.1f}')
    cont+=1