from cmath import sqrt

linha = input()
a,b,c = linha.split(" ")

delta = float(b)**2 - (4 * float(a) * float(c))
if delta < 0:
    print("Impossivel calcular ")
else:
    try:
        r1 = (-float(b) + sqrt(delta)) / (2 * float(a))
        r2 = (-float(b) - sqrt(delta)) / (2 * float(a))
        print("R1 = {:.5f}".format(r1))
        print("R1 = {:.5f}".format(r2))
    except:
        print("Impossivel calcular ")