def serie_dado(serie_lancamentos=input('Digite a série de lancamentos, separando cada caso com um espaço: ')):
    """
    Essa função recebe uma série de lançamentos de dados e retorna quantos elementos duplicados adjacentes têm;
    str -> int
    """
    temp = serie_lancamentos.split(' ')
    lista = [int(x) for x in temp]
    contador = 0
    consecutivos = 0
    while contador < len(lista)-1:
        if lista[contador] == lista[contador -1] and lista[contador] != lista[contador+1]:
            consecutivos += 1
        contador += 1
    return consecutivos
                     

def programa_que_le_i(a,b,c,i= input('Digite um número entre 1 e 4')):
    """
    Essa função recebe três números inteiros a,b,c e um número entre 1 e 4 e retorna:
    caso i = 1: a área do trapézio com a, b de bases e c de altura;
    i = 2: os a, b, c ao quadrado;
    i = 3: a média aritmética entre a,b,c;
    i = 4: a soma dos inteiros de a até b  com uma variação igual a c;
    """
    if int(i) == 1:
        return print(((a+b) * c)/ 2, f'a={a},b={b},c={b}')
    elif int(i) == 2:
        return print(a*a, b*b, c*c, f'a={a},b={b},c={b}')
    elif int(i) == 3:
        return print((a+b+c)/3, f'a={a},b={b},c={b}')
    elif int(i) == 4:
        soma = 0
        for x in range(a, b+1, c):
            soma += x
        return print(soma, f'a={a},b={b},c={b}')
    

def buscarSetor(setor):
    """
    Essa função recebe o input dos dados dos funcionários e o setor, e retorna os dados dos funcionários daquele setor;
    str, str -> list
    """
    matriz = []
    P = input('Digite o número de funcionários: ')
    n_funcionarios = int(P)
    contador = 0
    while contador < n_funcionarios:
        P = input('Digite os dados de um funcionário, separando-os com um espaço: ')
        dados = P.split(' ')
        matriz.append(dados)
        contador += 1
    matriz_resultado = []
    for i in matriz:
        if setor in i:
            matriz_resultado.append(i)
    for i in matriz_resultado:
        list.pop(i, 2)
    if matriz_resultado == []:
        return "Nenhum registro encontrado"
    return matriz_resultado



"""
Não (a e b)


"""


def invertido(str):
    return str[::-1]

print(invertido('José Moisés Pereira da Silva Fortunato'))
