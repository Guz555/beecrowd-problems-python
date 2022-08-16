t = int(input())

for i in range(0,t):
    pa,pb,g1,g2 = map(float, input().split())
    pa = int(pa)
    pb = int(pb)
    ano = 0
    while pb>=pa:
        pa = int(pa*(1 + g1/100))
        pb = int(pb*(1 + g2/100))
        #print('PA {} e o PB {}'.format(pa,pb))
        ano = ano + 1
        if ano >=101:
            print('Mais de 1 seculo.')
            break
    if ano <=100:
        ano = int(ano)
        print('{} anos.'.format(ano)) 



"""pa, pb, g1, g2 = input().split()
c1 = (float(g1) * int(pa)) / 100
c2 = (float(g2) * int(pa)) / 100


con = 0
while int(pb) >= int(pa):
    pa = int(pa) + c1
    pb = int(pb) + c2
    if con > 100:
            break 
    con+= 1
    #print(pa, con, pb)"""



