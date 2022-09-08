n = input()
lista = []
for x in range(0,int(n)):
    n1 = input()
    # lista = [x for x in range(1,int(n1)) if int(n1) % x == 1 and int(n1) % x == int(n1)]    
    for x in range(2, int(n1) +1):
        lista.append(x)
    
    for x in lista:
        if int(n1) != x and int(n1) % x == 0:
            print(f'{n1} nao eh primo')
            break
        else:
            print(f'{n1} eh primo')
            break
   

    