vitIn = 0
vitGr = 0
jogos = 0
empate = 0
vencedor = ''
res = 0

while int(res) != 2:
    linha = input().split()
    i, g = linha
    jogos += 1
    print("Novo grenal (1-sim 2-nao)")
    if int(i) > int(g):
        vitIn += 1
    elif int(g) > int(i):
        vitGr += 1
    elif int(g) == int(i):
        empate += 1
    i, g = linha
    res = input()

if vitGr > vitIn:
    vencedor = 'Gremio'
elif vitIn > vitGr:
    vencedor = 'Inter'
else:
    vencedor = None

print(f"{jogos} grenais")
print(f'Inter:{vitIn}')
print(f'Gremio:{vitGr}')
print(f'Empates:{empate}')
if not vencedor:
    print('Nao houve vencedor')
else:
    print(vencedor,'venceu mais')
