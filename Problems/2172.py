x, m = input().split()

total_xp = []

while int(x) != 0 and int(m) != 0:
    res = int(x) * int(m)
    total_xp.append(res)
    x, m = input().split()

for n in total_xp:
    print(n)
