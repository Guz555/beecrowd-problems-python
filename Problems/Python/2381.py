alunos = []

n, k = input().split()

for x in range(0,int(n)):
    a = input()
    alunos.append(a)

alunos = sorted(alunos)
print(alunos[int(k) -1])
