t = int(input())
res = []
for x in range(0, t):
    q = int(input())
    n1=1
    for x in range(0, q):
        n1+=n1
    n1 = int((n1 / 12) / 1000)
    res.append(n1)

for x in res:
    print(f'{x} kg')