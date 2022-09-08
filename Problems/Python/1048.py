salario = input()
aumento = 0.00
reajuste = 0
perc = ''
if float(salario) <= 400:
    aumento = float(salario) * 1.15
    reajuste = float(salario) * 0.15
    perc = '15 %'
elif float(salario) > 400 and float(salario) <= 800:
    aumento = float(salario) * 1.12
    reajuste = float(salario) * 0.12
    perc = '12 %'
elif float(salario) > 800 and float(salario) <= 1200:
    aumento = float(salario) * 1.1
    reajuste = float(salario) * 0.1
    perc = '10 %'
elif float(salario) > 1200 and float(salario) <= 2000:
    aumento = float(salario) * 1.07
    reajuste = float(salario) * 0.07
    perc = '7 %'
elif float(salario) > 2000:
    aumento = float(salario) * 1.04
    reajuste = float(salario) * 0.04
    perc = '4 %'

print(f'Novo salario: {aumento:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {perc}')
