n = int(input())
if n == 0:
    r = 'E'
elif n >= 1 and n <= 35:
    r = 'D'
elif n >= 36 and n <= 60:
    r = 'C'
elif n >= 61 and n <= 85:
    r = 'B'
elif n >= 86:
    r = 'A'

print(r)
