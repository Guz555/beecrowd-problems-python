positivos = 0
negativos = 0
pares = 0
impares = 0

for x in range(0,5):
    n = input()
    if int(n) > 0:
        positivos += 1
    if int(n) < 0:
        negativos += 1
    if int(n) % 2 == 0:
        pares += 1
    if int(n) % 2 != 0:
        impares += 1

print(pares,"valor(es) par(es)")
print(impares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")
