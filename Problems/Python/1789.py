while True:
    try:
        n = int(input())
        v = input().split()
        vMax = int(max(v))
        if vMax >= 20:
            nivel = 3
        elif vMax < 20 or vMax >= 10:
            nivel = 2
        elif vMax < 10:
            nivel = 1
        print(nivel)
    except EOFError:
        break