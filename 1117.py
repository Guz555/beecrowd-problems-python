lista = []
lista2 = []
notaValida = 0
while True:
    nota = input()
    if float(nota) < 0 or float(nota) > 10:
        lista.append("nota invalida")
    else:
        notaValida += 1
        lista2.append(float(nota))
    if  notaValida > 1:
        break   
    
for x in lista:
    print(x)

lista2 = (sum(lista2)) / 2

print(f"media = {lista2:.2f}")