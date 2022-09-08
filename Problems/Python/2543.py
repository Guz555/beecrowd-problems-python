"""n, i = input().split()
id = []
for x in range(0, int(n)):
    i, j = input().split()
    id.append([int(i), int(j)])

print(id.count([i, 0]))"""
while True:
    try:
        n, iden = input().split()
        qt = 0
        n = int(n)
        while n > 0:
            n -= 1
            j, g = input().split()
            if j == iden and g == '0':
                qt += 1
        print(qt)

    except EOFError:
        break
