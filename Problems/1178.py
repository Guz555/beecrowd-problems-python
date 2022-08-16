n = float(input())
l = []

l.append(n)

for x in range(0, 99):
    n = n / 2
    l.append(n)

c = 0
for x in l:
    print(f'N[{c}] = {x:.4f}')
    c += 1
