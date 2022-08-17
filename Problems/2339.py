from os import F_OK


c, f, f1 = input().split()

if float(f) / float(f1) >= float(c):
    print('S')

elif float(f) / float(f1) <= float(c):
    print('N')
