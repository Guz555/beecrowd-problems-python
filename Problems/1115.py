linha = input().split()
x, y = linha
lis = []
while True:
    if int(x) > 0 and int(y) > 0:
        lis.append("primeiro")
    elif int(x) > 0 and int(y) < 0:
        lis.append("quarto")
    elif int(x) < 0 and int(y) < 0:
        lis.append("terceiro")
    elif int(x) < 0 and int(y) > 0:
        lis.append("segundo")
    elif int(x) == 0 or int(y) == 0:
        break
    linha = input().split()
    x, y = linha

for x in lis:
    print(x)