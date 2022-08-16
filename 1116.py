n = input()
lis = []
for x in range(0,int(n)):
    linha = input().split()
    n1, n2 = linha
    if int(n2) == 0:
        lis.append("divisao impossivel")
    else:
        r = float(n1) / float(n2)
        lis.append(f"{r:.1f}")
    

for x in lis:
    print(x)