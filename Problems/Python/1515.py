while True:
    n = int(input())
    if not n: break
    planeta = []
    ano = []
    for x in range(0, n):
        p, a, t = input().split()
        planeta.append(p)
        menor = int(a) - int(t)
        ano.append(menor)

    print(planeta[ano.index(min(ano))])
