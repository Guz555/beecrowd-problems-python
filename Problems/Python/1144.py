n = input()
c = 1
c2 = 1
c3 = 0
v = 2
for x in range(0, int(n)):
    c3 = c * c2
    for x in range(0, 2):  
        print(c, c2, c3)
        c2 += 1
        c3 += 1

    c2 -= 1 
    c+= 1
    c2+= v
    v+= 2
    

    
    