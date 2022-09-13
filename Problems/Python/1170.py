n = int(input())
d = []
for x in range(0, n):
    s = input()
    c = 0
    while float(s) > 1:
        s = float(s) / 2
        c+= 1
    d.append(c)

for x in d:
    print(f'{x} dias')