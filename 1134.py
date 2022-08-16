n = input()
alc = 0 
gas = 0
die = 0
while int(n) != 4:
    if int(n) == 1:
        alc += 1
    elif int(n) == 2:
        gas += 1
    elif int(n) == 3:
        die += 1
    n = input()

print("MUITO OBRIGADO")
print("Alcool:",alc)
print("Gasolina:",gas)
print("Diesel:",die)
