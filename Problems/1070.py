x = input()

if int(x) % 2 != 0:
    print(x)
    for n in range(0,5):
        x = int(x) + 2
        print(x)
elif int(x) % 2 == 0:
    x = int(x) + 1
    print(int(x))
    for n in range(0,5):
        x = int(x) + 2
        print(x)
       
 