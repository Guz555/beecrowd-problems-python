num = input()
coelho = 0
rato = 0
sapo = 0
cobaia = 0

totalCobaia = 0

for x in range(0, int(num)):
    c = input().split()
    n, a = c
    totalCobaia += int(n)
    if a == 'C':
        coelho += int(n)
    if a == 'R':
        rato += int(n)
    if a == 'S':
        sapo += int(n)

porCoelho = (coelho / totalCobaia) * 100
porRato = (rato / totalCobaia) * 100
porSapo = (sapo / totalCobaia) * 100

print("Total:",totalCobaia,'cobaias')
print('Total de coelhos:',coelho)
print('Total de ratos:',rato)
print('Total de sapos:',sapo)
print(f'Percentual de coelhos: {porCoelho:.2f} %')
print(f'Percentual de ratos: {porRato:.2f} %')
print(f'Percentual de sapos: {porSapo:.2f} %')

