n = input()
dentro = 0
fora = 0

for x in range(0, int(n)):
    n1 = input()
    if int(n1) not in range(10,21):
        fora += 1
    else:
        dentro+=1
        
print(dentro, 'in')
print(fora,'out')