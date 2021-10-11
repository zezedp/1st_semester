def excluir_telefone(lista, telefone):
    """
    Essa função recebe uma lista e um telefone, e caso 
    o telefone esteja na lista, ela retornará se foi excluido 
    ou não o número de telefone da lista;
    list, str -> bool
    """
    lista1 = lista[1]
    tel = ''.join(lista1)
    if telefone == tel:
        lista[1].remove(telefone)
        return True
    return False


def campeonato(tabela):
    """
    Essa função recebe uma lista (tabela) no seguinte formato:
    [
        [time1, pontos1],
        [time2, pontos2],
        [time1, pontos1_2fase],
        [time2, pontos1_2fase]
    ]

    e retorna uma lista contendo os nomes dos times no campeonato, 
    a quantidade de pontos do time campeão e as médias de pontos dos times;
    list -> list
    """
    time1 = tabela[0][0]
    time2 = tabela[1][0]
    pontos1 = tabela[0][1]
    pontos2 = tabela[1][1]
    pontos1_2fase = tabela[2][1]
    pontos2_2fase = tabela[3][1]

    total_time1 = pontos1 + pontos1_2fase
    total_time2 = pontos2 + pontos2_2fase
    media_time1 = (pontos1 + pontos1_2fase) / 2
    media_time2 = (pontos2 + pontos2_2fase) / 2

    if total_time1 > total_time2:
        return [[time1, time2, [total_time1], [media_time1, media_time2]]]
    if total_time1 < total_time2:
        return [[time2, time1, [total_time2], [media_time1, media_time2]]]
