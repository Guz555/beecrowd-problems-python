linha = input().split(" ")
a = b = c = 0
n1,n2,n3 = linha
if float(n1) >= float(n2) and float(n1) >= float(n3):
    a = n1
    if float(n2) >= float(n3):
        b = n2
        c = n3
    else:
        b = n3
        c = n2
elif float(n2) >= float(n1) and float(n2) >= float(n3):
    a = n2
    if float(n1) >= float(n3):
        b = n1
        c = n3
    else:
        b = n3
        c = n1
elif float(n3) >= float(n1) and float(n3) >= float(n2):
    a = n3
    if float(n2) >= float(n1):
        b = n2
        c = n1
    else:
        b = n1
        c = n2


if float(a) >= float(b) + float(c):
    print("NAO FORMA TRIANGULO")

elif (float(a)**2) == (float(b)** 2) + (float(c) ** 2):
    print("TRIANGULO RETANGULO")

elif (float(a)** 2) > (float(b)** 2) + (float(c) ** 2):
    print("TRIANGULO OBTUSANGULO")

elif (float(a)** 2) < (float(b)** 2) + (float(c) ** 2):
    print("TRIANGULO ACUTANGULO")

if float(a) == float(b) and float(a) == float(c):
    print("TRIANGULO EQUILATERO")

elif float(a) == float(b) or float(a) == float(c) or float(b) == float(c):
    print("TRIANGULO ISOSCELES")

