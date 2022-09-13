resultado = []
while True:
    try:
        m, n = input().split()

        m = [x for x in range(1, int(m) + 1)]
        n = [x for x in range(1, int(n) + 1)]

        res = 1
        res2 = 1
        for x in m:
            res*= x
        for x in n:
            res2 *= x
        res += res2

        resultado.append(res)
    except EOFError:
        break
    
for n in resultado:
    print(n)