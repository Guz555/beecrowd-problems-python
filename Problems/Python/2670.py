a1 = input()
a2 = input()
a3 = input()

andares = [int(a1), int(a2), int(a3)]
maior = max(andares)

if andares.index(maior) == 2:
    r = andares[0] * 4
    r += andares[1] * 2
if andares.index(maior) == 1:
    r = andares[0] * 2
    r += andares[2] * 2
if andares.index(maior) == 0:
    r = andares[1] * 2
    r += andares[2] * 4

print(r)