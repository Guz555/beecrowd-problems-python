n1 = input()
n2 = input()
if int(n1) < int(n2):
    for x in range(int(n1)+1, int(n2)+1):
        if x % 5 == 2 or x % 5 == 3:
            print(x)
            
else:
    for x in range(int(n2)+1, int(n1)+1):
        if x % 5 == 2 or x % 5 == 3:
            print(x)
 