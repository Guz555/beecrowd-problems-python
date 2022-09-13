n = int(input())

for x in range(0, n):
    y,z = input().split()
    if z == 'bin':
        y = int(y // 2)