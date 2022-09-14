n = int(input())
for x in range(0, n):
    num = int(input())
    cont = 0
    for x in range(2, num):
        if num % x == 0:
            cont+= 1
            break
    if cont == 0:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
    