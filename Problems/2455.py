p1, c1, p2, c2 = input().split()

esquerdo = int(p1) * int(c1)
direito = int(p2) * int(c2)

if esquerdo == direito:
    print(0)
elif esquerdo > direito:
    print(-1)
elif esquerdo < direito:
    print(1)
