a = int(input())
l = []

for x in range(0, a):
    t, d = input().split()
    res = int(t) * int(d)
    l.append(res)

print(sum(l))
