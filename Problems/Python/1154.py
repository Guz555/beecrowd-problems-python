media = []
n = input()
while float(n) >= 0:
    media.append(int(n))
    n = input()

res = sum(media) / len(media)
print(f'{res:.2f}')