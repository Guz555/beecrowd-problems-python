linha = input().split()
a,b,c = linha
perimetro = 0
area = 0

if abs(float(b) - float(c)) < float(a) and float(a) < float(b) + float(c):
    perimetro = float(a) + float(b) + float(c)
    print(f"Perimetro = {perimetro:.1f}")

elif abs(float(a) - float(c)) < float(b) and float(b) < float(a) + float(c):
    perimetro = float(a) + float(b) + float(c)
    print(f"Perimetro = {perimetro:.1f}")

elif abs(float(c) - float(b)) < float(a) and float(a) < float(b) + float(c):
    perimetro = float(a) + float(b) + float(c)
    print(f"Perimetro = {perimetro:.1f}")

elif abs(float(a) - float(b)) < float(c) and float(c) < float(a) + float(b):
     perimetro = float(a) + float(b) + float(c)
     print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((float(a) + float(b)) * float(c)) / 2
    print(f"Area = {area:.1f}")
