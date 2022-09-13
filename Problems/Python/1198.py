while True:
    try:
        n1, n2 = input().split()
        res = abs(int(n2) - int(n1))
        print(res)
    except EOFError:
        break