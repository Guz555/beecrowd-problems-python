num = int(input())
cont = 0
for x in range(2, num):
    if num % x == 0:
        cont += 1
        break
if cont == 0:
    print('primo')
else:
    print('não primo')

l = [1, 2, 3, 4, 5]
res = sum(l[::3])
print(res)
