linha = input().split(" ")
a,b,c = linha

maiorab =  (int(a) + int(b) + abs(int(a)-int(b))) / 2 
maiorc = (maiorab + int(c) + abs(maiorab-int(c))) / 2

print(f"{int(maiorc)} eh o maior")

 