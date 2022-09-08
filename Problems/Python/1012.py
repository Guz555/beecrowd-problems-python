linha = input().split(" ")
a,b,c = linha

pi = 3.14159
triangulo = ((float(a) * float(c)) / 2)
circulo = (pi * (float(c)**2))
trapezio = (((float(a) + float(b)) * float(c))) / 2
quadrado = float(b)**2
retangulo = (float(a) * float(b))

print("TRIANGULO:",f'{triangulo:.3f}')
print("CIRCULO:",f'{circulo:.3f}')
print("TRAPEZIO:",f'{trapezio:.3f}')
print("QUADRADO:",f'{quadrado:.3f}')
print("RETANGULO:",f'{retangulo:.3f}')
 