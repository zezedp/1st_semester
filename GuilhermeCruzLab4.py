def SIGA(tupla_dados):
    """
    Essa função recebe o nome do aluno, suas 3 notas e 
    retorna uma tupla dizendo se o aluno foi aprovado ou não;
    tuple -> tuple
    """
    nome, nota1, nota2, nota3 = tupla_dados
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return (nome, round(media, 1), 'aprovado', 'Parabéns!')
    elif media >= 5:
        return (nome, round(media, 1), 'aprovado')
    return (nome, round(media, 1), 'reprovado')


def zodiaco_chines_sem_if(ano_nascimento):
    # Sem usar o if
    """
    Essa função recebe o ano de nascimento de uma pessoa 
    e retorna o seu animal no zodíaco chinês;
    int -> str
    """
    dicionario_zodiaco = {
        0: "Macaco",
        1: "Galo",
        2: "Cão",
        3: "Porco",
        4: "Rato",
        5: "Boi",
        6: "Tigre",
        7: "Coelho",
        8: "Dragão",
        9: "Serpente",
        10: "Cavalo",
        11: "Carneiro"
    }

    idade_animal = ano_nascimento % 12
    return dicionario_zodiaco[idade_animal]


def zodiaco_chines_com_if(ano_nascimento):
    # Usando o if
    """
    Essa função recebe o ano de nascimento de uma pessoa 
    e retorna o seu animal no zodíaco chinês;
    int -> str
    """
    lista_animais = ["Macaco","Galo","Cão","Porco","Rato","Boi","Tigre","Coelho","Dragão","Serpente","Cavalo","Carneiro"]
    ano_animal = ano_nascimento % 12
    for i in range(11):
        if ano_animal == i:
            return lista_animais[ano_animal]
        else:
            i += 1


def telefone(numero_telefone):
    """
    Essa função recebe um número de telefone e retorna 
    uma tupla contendo uma string com seu ddd e outra com 
    o resto do número;
    int -> tuple
    """
    numero_telefone = str(numero_telefone)
    ddd = numero_telefone[:2]
    telefone_sem_ddd = numero_telefone[2:]
    if len(numero_telefone) < 10:
        return ('', '')
    return (ddd, telefone_sem_ddd)


def formato_data(data):
    """
    Essa função recebe uma data em formato de string e retorna quais as possibilidades 
    de arranjar essa data, seja yy/mm/dd, mm/dd/yy e/ou dd/mm/yy;
    str -> tuple
    """
    if 0 < int(data[:2]) <= 12 and int(data[4:5]) <= 12 and 0 < int(data[6:]) <= 12:
        return ('dd/mm/yy', 'mm/dd/yy', 'yy/mm/dd')
    elif 0 < int(data[:2]) <= 12 and 0 < int(data[4:5]) <= 12:
        return ('dd/mm/yy', 'mm/dd/yy')
    elif int(data[:2]) > 12 and int(data[4:5]) <= 12 and int(data[6:]) > 12:
        return ('yy/mm/dd', 'dd/mm/yy')
    elif int(data[:2]) > 12  and int(data[4:5]) <= 12 and int(data[6:]) > 12:
        return ('dd/mm/yy')
    elif int(data[:2]) <= 12 and int(data[4:5]) > 12 and int(data[6:]) > 12:
        return ('mm/dd/yy')
    elif 0 <= int(data[4:5]) <= 12 and 0 < int(data[6:]) <= 31:
        return ('yy/mm/dd')
    return ()
