linha = input().split()
x, y = linha
lis = []
while int(x) != int(y):
    if int(x) > int(y):
        lis.append('Decrescente')
    else:
        lis.append('Crescente')
    
    linha = input().split()
    x, y = linha

for x in lis:
    print(x)