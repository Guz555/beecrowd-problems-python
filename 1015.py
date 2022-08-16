import math

p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2

dsitancia = (((float(x2))-(float(x1)))**2) + (((float(y2)) - (float(y1)))**2)
distancia_final = math.sqrt(dsitancia)

print(f"{distancia_final:.4f}")
