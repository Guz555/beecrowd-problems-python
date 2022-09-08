cpf = input()

res = cpf.split('.')
dd = res[2].split('-')
res.pop()

for x in res:
    print(x)

for x in dd:
    print(x)
