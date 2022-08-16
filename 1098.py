i = 0
j = 0
for x in range(0,11):
    j += i
    for x in range(0,3):
        
        print(f"I={i:.1f} J={j}")    
        j += 1
    i += 0.2
    j = 1


"""
i = 0
j = 0
k = 0.2
for x in range(0,11):
    for x in range(0,3):
        j += 1
        if i % 1 > 0 and i % 1 != 0.9999999999999998:
            print(f"I={i:.1f} J={j:.1f}")
        elif i < 2:
            print(f"I={int(i)} J={int(j)}")
        else: 
            print(f"I={int(i)} J={int(j)}")
    j = 0
    i += 0.2
    j += i



"""