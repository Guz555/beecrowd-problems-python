nome = input()
salario = float(input())
total_vendas = float(input())

total = (total_vendas * 0.15) + salario

print("TOTAL = R$",f'{total:.2f}')
