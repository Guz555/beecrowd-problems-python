n = int(input())

for x in range(0, n):
    cont = 0
    num = int(input())
    for x in range(2, num):
        if num % x == 0:
            cont += 1
            break
    if cont == 0:
        print('Prime')
    else:
        print('Not Prime')