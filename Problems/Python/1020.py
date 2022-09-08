n1 = int(input())
ano = dia = mes = 0

if n1 >= 365:
    ano = n1 / 365
    mes = (n1 % 365) / 30 
    dia = (n1 % 365) % 30
else:
    mes = n1 / 30
    dia = n1 % 30

print(int(ano), "ano(s)")
print(int(mes), "mes(es)")
print(int(dia), "dia(s)")


