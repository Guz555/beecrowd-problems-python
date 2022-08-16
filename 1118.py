
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
    if notaValida > 1:
        notaValida = 0
        for x in lista:
            print(x)
        lista2 = (sum(lista2)) / 2
        print(f"media = {lista2:.2f}")
        print("novo calculo (1-sim 2-nao)")
        n = input()
        lista = []
        lista2 = []
        while n != 1:
            if int(n) == 1:
                break
            elif int(n) == 2:
                break
            else:      
                print("novo calculo (1-sim 2-nao)")
                n = input()
        if int(n) == 2:
            break
        else:
            continue