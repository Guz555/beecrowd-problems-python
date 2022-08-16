matriz = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
]
lista = []

entrada = float(input())
tipo = input()
for n in range(0, len(matriz)):

    tamanho_lista = len(matriz[int(entrada)])

    matriz[int(entrada)].clear()
    for x in range(0, tamanho_lista):
        novo_num = float(input())
        matriz[int(entrada)].append(novo_num)
        lista.append(novo_num)

    if not entrada >= len(matriz) - 1:
        entrada += 1
    else:
        entrada = 0

    if tipo == 'S':
        res = sum(lista)
    elif tipo == 'M':
        for linha in matriz:
            for num in lista:
                lista.append(num)
        res = sum(lista)/sum(lista)

print(f'{res:.1f}')
