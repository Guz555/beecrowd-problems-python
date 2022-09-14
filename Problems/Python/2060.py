b = input()
a = input().split()
mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0
for x in a:
    if int(x) % 2 == 0:
        mult2 += 1

    if int(x) % 3 == 0:
        mult3 += 1
    
    if int(x) % 4 == 0:
        mult4 += 1
    
    if int(x) % 5 == 0:
        mult5 += 1

print(f"{mult2} Multiplo(s) de 2")
print(f"{mult3} Multiplo(s) de 3")
print(f"{mult4} Multiplo(s) de 4")
print(f"{mult5} Multiplo(s) de 5")
