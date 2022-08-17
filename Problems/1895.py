qtd = int(input())
valor_total = []

for x in range(0, qtd):
    p, q = input().split()
    if int(p) == 1001:
        p = 1.5
    elif int(p) == 1002:
        p = 2.5
    elif int(p) == 1003:
        p = 3.5
    elif int(p) == 1004:
        p = 4.5
    elif int(p) == 1005:
        p = 5.5

    res = float(p) * float(q)
    valor_total.append(res)

t = sum(valor_total)
print(f'{t:.2f}')
