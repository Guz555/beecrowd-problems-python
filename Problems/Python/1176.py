t = int(input())
for x in range(0, t):

    n = int(input())
    num1 = 0
    num2 = 1
    c = 0

    while c < n:
        num = num1 + num2
        num2 = num1
        num1 = num
        c += 1

    print(f'Fib({n}) = {num1}')
