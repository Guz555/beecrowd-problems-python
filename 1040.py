linha = input().split(" ")
n1,n2,n3,n4 = linha

media = ((float(n1) * 2) + (float(n2) * 3) + (float(n3) * 4) + (float(n4) * 1))  / (2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media < 6.9:
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    n_final = (n5 + media) / 2
    if n_final >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {n_final:.1f}")
    elif n_final <= 4.9:
        print("Aluno reprovado.")
        print(f"Media final: {n_final:.1f}")
