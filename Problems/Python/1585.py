n = int(input())
l= []
for x in range(0, n):
    d1, d2 = input().split()
    res = (int(d1) * int(d2) / 2)
    l.append(res)

for x in l:
    print(f'{int(x)} cm2')