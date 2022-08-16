media = 0
lista = []
positivos = 0
for x in range(1,7):
    n = input()
    lista.append(float(n))

for x in lista:
    if x > 0:
        positivos+= 1
        media += x

media = media / positivos
print(positivos,"valores positivos")
print(f"{media:.1f}")