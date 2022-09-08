n = int(input())
l = []
n2 = input().split()

for x in n2:
    l.append(int(x))


menor = min(l)
pos = l.index(menor)

print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')
