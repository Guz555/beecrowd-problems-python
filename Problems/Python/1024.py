num = input()
frases = []
for x in range(0, int(num)):
    tx = input()
    frases.append(tx)


def primeiro_passo(txt) -> str:
    lista = []
    textofinal = []
    for x in txt:
        lista.append(ord(x))
    
    for x in lista:
        if chr(x).isalpha():
            x += 3
        textofinal.append(chr(x))

    textofinal = "".join(textofinal)
    return textofinal

def segundo_passo(txt) -> str:
    txt = txt[::-1]
    return txt

def terceiro_passo(txt) -> str:
    contador = 0
    metade = int(len(txt) / 2)
    parte1 = []
    parte2 = []
    lista = []
    listaFinal = []
    for x in txt:
        contador += 1
        if contador <= metade:
            parte1.append(x)
    
    contador = 0
    for x in txt:
        
        contador += 1
        if contador > metade:
            parte2.append(x)
        
    for x in parte2:
        lista.append(ord(x) - 1)
    
    for x in lista:
        listaFinal.append(chr(x))
    
    parte1 = ''.join(parte1)
    listaFinal = ''.join(listaFinal)

    return parte1 + listaFinal
    
    
for x in frases:
    x = primeiro_passo(x)
    x = segundo_passo(x)
    x = terceiro_passo(x)
    print(x)
