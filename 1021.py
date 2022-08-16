nota = float(input())
moeda =  nota - int(nota)
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0
moeda1 = moeda50 = moeda25 = moeda010 = moeda05 = moeda001 = 0

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
    moeda1 = nota 

if moeda >= 0.5:
    moeda50 = moeda / 0.5
    moeda = moeda % 0.5

if moeda >= 0.25:
    moeda25 = moeda / 0.25
    moeda = moeda % 0.25

if moeda >= 0.1:
    moeda010 = moeda / 0.1
    moeda = moeda % 0.1

if moeda >= 0.05:
    moeda25 = moeda / 0.05
    moeda = moeda % 0.05

if moeda >= 0.01:
    moeda001 = moeda / 0.01

print("NOTAS:")
print(f'{int(notas100)} nota(s) de R$ 100.00')
print(f'{int(notas50)} nota(s) de R$ 50.00')
print(f'{int(notas20)} nota(s) de R$ 20.00')
print(f'{int(notas10)} nota(s) de R$ 10.00')
print(f'{int(notas5)} nota(s) de R$ 5.00')
print(f'{int(notas2)} nota(s) de R$ 2.00')
print("MOEDAS:")
print(f'{int(moeda1)} moeda(s) de R$ 1.00')
print(f'{int(moeda50)} moeda(s) de R$ 0.50')
print(f'{int(moeda25)} moeda(s) de R$ 0.25')
print(f'{int(moeda010)} moeda(s) de R$ 0.10')
print(f'{int(moeda05)} moeda(s) de R$ 0.05')
print(f'{int(moeda001)} moeda(s) de R$ 0.01')


