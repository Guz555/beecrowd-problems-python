nota = int(input())
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0
print(nota)

if nota >= 100:
    notas100 = nota / 100
    nota = nota % 100

if nota >= 50:
    notas50 = nota / 50
    nota = nota % 50

if nota >= 20:
    notas20 = nota / 20
    nota = nota % 20

if nota >= 10:
    notas10 = nota / 10
    nota = nota % 10

if nota >= 5:
    notas5 = nota / 5
    nota = nota % 5

if nota >= 2:
    notas2 = nota / 2
    nota = nota % 2

if nota >= 1:
    notas1 = nota 
    
print(f'{int(notas100)} nota(s) de R$ 100,00')
print(f'{int(notas50)} nota(s) de R$ 50,00')
print(f'{int(notas20)} nota(s) de R$ 20,00')
print(f'{int(notas10)} nota(s) de R$ 10,00')
print(f'{int(notas5)} nota(s) de R$ 5,00')
print(f'{int(notas2)} nota(s) de R$ 2,00')
print(f'{int(notas1)} nota(s) de R$ 1,00')
