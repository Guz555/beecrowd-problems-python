valor = input()
n = 0
if float(valor) <= 2000.00:
    print("Isento")
elif float(valor) > 2000.00 and valor <= 3000.00:
    n = float(valor) - 2000.00
