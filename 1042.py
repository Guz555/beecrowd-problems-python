
linha = input().split()

n1,n2,n3 = linha
maior = meio = menor = 0
if int(n1) > int(n2) and int(n1) > int(n3):
    maior = n1
    if int(n2) > int(n3):
        meio = n2
        menor = n3
    else:
        meio = n3
        menor = n2
elif int(n2) > int(n1) and int(n2) > int(n3):
    maior = n2
    if int(n1) > int(n3):
        meio = n1
        menor = n3
    else:
        meio = n3
        menor = n1
elif int(n3) > int(n1) and int(n3) > int(n2):
    maior = n3
    if int(n2) > int(n1):
        meio = n2
        menor = n1
    else:
        meio = n1
        menor = n2

print(menor)
print(meio)
print(maior)
print()
print(n1)
print(n2)
print(n3)