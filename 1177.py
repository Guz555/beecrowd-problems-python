t = int(input())
l = []
c = 0
for x in range(0, 1000):
    l.append(c)
    c += 1
    if c == t:
        c = 0

c = 0
for x in l:
    print(f'N[{c}] = {x}')
    c += 1
