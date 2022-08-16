par = []
impar = []
par2 = []
impar2 = []

for x in range(0, 71):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(par)
print(impar)
