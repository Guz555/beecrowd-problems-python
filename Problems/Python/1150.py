x = input()
z = input()

soma = [int(x)]
while int(z) <= int(x):
    z = input()

while sum(soma) < int(z):
    x = int(x) + 1
    soma.append(x)

print(len(soma))