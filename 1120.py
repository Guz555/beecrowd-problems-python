from operator import contains


d = 1
n = 1

while int(d) != 0 and int(n) != 0:
    d, n = input().split()
    l = []
    for x in n:
        if x in d:
            continue
        l.append(x)
    l = ''.join(l)
    print(l)