linha = input().split()
hi, mi, hf, mf = linha

horaTotal = int(hi) * 60 + int(mi)
horaFinal = int(hf) * 60 + int(mf)
resto = 0
minuto = 0
hora = 0
if horaFinal > horaTotal:
    resto = horaFinal - horaTotal
    hora = int(resto / 60)
    minuto = int(resto % 60)
elif horaTotal > horaFinal:
    hora = int(hi) - int(hf)
    hora = 24 - hora
    minuto = int(mi) - int(mf)
    minuto = 60 - minuto

    

print("O JOGO DUROU",hora,"HORA(S) E",minuto,"MINUTO(S)")

