import math

def qtd_elem(iteravel, elem):
    """
    Essa função recebe um valor iteravel str, list ou tuple e 
    um elemento, retornando quantas vezes esse elelemtnso aparece em iteravel;
    str/list/tuple, str -> int
    """
    resultado = {}
    for i in iteravel:
        if not i in resultado:
            resultado[i] = 1
        else:
            resultado[i] += 1
    for y, x in resultado.items():
        if y == elem:
            return x


def qtd_elem_trecho(iteravel, elem, ini, fim):
    """
    Essa função recebe um iterável, um elemento, o início e o fim de um trecho do iterável e 
    retorna quantas vezes o elem aparece no trecho do iterável incluindo o inicio e o fim;
    str/list/tuple, str, int, int -> int
    """
    final = fim + 1
    iteravel_novo = iteravel[ini:final]
    return qtd_elem(iteravel_novo, elem)


def atualiza_mascara(secreto, mascara_atual, letra):
    """
    Essa função recebe a palavra secreta (secreto), a máscara atual e a letra que 
    o usuário escolheu e retorna a máscara atualizada caso a letra esteja no secreto;
    str, list, str -> list
    """
    contador = 0
    for x in secreto:
        if letra == x:
             mascara_atual[contador] = letra
        contador += 1
    return mascara_atual
    

def soma_serie(n):
    """
    Essa função recebe o número de termos para somar a série e retorna a soma da série;
    int -> float
    """
    resultado = 1
    contador = 1
    for i in range(3, n+1, 2):
        if contador % 2 == 0:
            resultado += 1/i
            contador += 1
            continue
        else:
            resultado -= 1/i
            contador += 1
            continue
    return resultado


def soma_serie_b():
    """
    Essa função retorna quantos termos são necessários para que o erro entre da 
    soma da série e o valor para o qual a soma converge chegue a inferior a 0.01;
        -> tuple
    """
    for i in range(100):
        if math.fabs(soma_serie(i) - (math.pi/4)) < 0.01:
            return (i, math.fabs(soma_serie(i) - (math.pi/4)))
