n, m = input().split()

for x in range(0, int(m)):
    acao = input()
    if acao == 'fechou':
        n = int(n) - 1
        n += 2
    elif acao == 'clicou':
        n = int(n) - 1

print(n)
