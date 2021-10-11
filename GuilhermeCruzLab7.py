from random import randint

def dados():
    """
    Essa função retorna quantas vezes os dois dados foram lançados 
    até que os dois dados sejam iguais;
       -> int
    """
    contador = 0
    while True:
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        if dado1 != dado2:
            contador += 1
            continue
        break
    return contador


def nome(contatos, nome):
    """
    Essa função recebe uma lista de contatos e um nome que o usuário deseja encontrar, 
    retornando assim o(s) nome(s) do(s) contato(s), caso não tenha ninguém salvo 
    na lista de contatos com esse nome, retornará uma lista vazia;
    list, str -> list
    """
    nomes = [x[0] for x in contatos]
    if nome == '' or nome == ' ':
        return []
    nome = nome.lower()
    resultado = []
    for i in nomes:
        if nome in i.lower():
            resultado.append(i)
    if resultado == []:
        return []
    return resultado
    