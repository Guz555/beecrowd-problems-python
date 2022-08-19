n = int(input())
op = input()

l = []
for x in range(0, 12):
    l.append([])

for x in range(0, 12):
    for y in range(0, 12):
        a = float(input())
        l[x].append(a)

if op == 'S':
    soma = 0
    for k in range(12):
        soma = soma + l[k][n]
    print(soma)
if op == 'M':
    med = 0
    soma = 0
    for k in range(12):
        soma = soma + l[k][n]
    med = soma/12
    print('{:.1f}'.format(med))
