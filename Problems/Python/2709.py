res = []
while True:
    try:
        m = int(input())
        l = []
        for x in range(0, m):
            v = int(input())
            l.append(v)

        p = int(input())
        num = sum(l[::p])
        cont = 0

        for x in range(2, num):
            if num % x == 0:
                cont += 1
                break
        if cont == 0:
            print(
                'You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError:
        break
