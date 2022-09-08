d, s = input().split()
saldo_atual = []
for x in range(0, int(d)):
    deposito = int(input())
    s = int(s) + deposito
    saldo_atual.append(s)

print(min(saldo_atual))
