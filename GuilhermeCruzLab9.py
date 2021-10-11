def multiplica_matriz(matriz, n):
    """
    Essa função recebe uma matriz e um número e retorna a multiplicação dessa matriz pelo número;
    list, int -> list
    """
    matriz_nova = []
    for i in matriz:
        matriz_nova.append(i*n)
    return matriz_nova


def deu_match(afinidades):
    """
    Essa função recebe um dicionario 'afinidades' e retorna quem deu match com quem;
    dict -> list
    """
    k = []
    for i in afinidades:
        for j in afinidades.values():
            for x in j:
                if i in j:
                    k.append(i)
                    k.append(x)    
    subK = [k[n:n+2] for n in range(0, len(k), 2)]
    l = []
    c1 = 0
    print(1)
    while c1 <= len(subK) + 1:
        for i in subK:
            if i[0] != i[1]:
                l.append(i)
    t = ()
    for i in l:
        for x in range(len(l)):
            if i[c1] == reversed(i[x]) or reversed(i[c1]) == i[x] or i[c1] == i[x]:
                t += (i)
            c1 += 1
    return [t]


def quem_ligou(lista, telefone):
    """
    Essa função recebe uma lista de dados e um telefone, se esse telefone estiver na lista, 
    retornará os dados do contato que possui esse telefone;
    list, str -> list
    """
    for i in lista[1]:
        if telefone in i:
            return lista