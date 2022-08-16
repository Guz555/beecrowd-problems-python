linha = input().split()
hi, hf = linha

horario = int(hi) - int(hf)
if int(hi) < int(hf):
    horarioT = abs(int(hi) - int(hf))
else:
    horarioT = 24 - horario

print(f"O JOGO DUROU {horarioT} HORA(S)")