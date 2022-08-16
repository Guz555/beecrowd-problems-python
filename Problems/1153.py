n = input()
c = 1
for x in range(0, int(n)+1):
    if x == 0:
        continue
    c *= x
print(c)