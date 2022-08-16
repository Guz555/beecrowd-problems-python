n1 = int(input())

min = (n1 / 60) % 60
hora = (n1 / 60) / 60
seg = n1 % 60
print(f"{int(hora)}:{int(min)}:{int(seg)}")
