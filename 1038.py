linha = input().split(" ")
cod, qtd = linha 
total = 0

if int(cod) == 1:
    total = float(qtd) * 4.0 

elif int(cod) == 2:
    total = float(qtd) * 4.5 

elif int(cod) == 3:
    total = float(qtd) * 5.0

elif int(cod) == 4:
    total = float(qtd) * 2.0

elif int(cod) == 5:
    total = float(qtd) * 1.5

print(f"Total: R$ {total:.2f}")
