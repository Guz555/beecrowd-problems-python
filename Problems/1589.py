num = int(input())
total = []
for x in range(0, num):
    r1, r2 = input().split()
    res = int(r1) + int(r2)
    total.append(res)

for n in total:
    print(n)
