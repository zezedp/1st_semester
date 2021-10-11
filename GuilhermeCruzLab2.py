import math

def media_3_inteiros(a, b, c):
    """
    Essa função recebe os parâmetros a, b, c e retorna a média aritmética entre eles;
    int, int, int -> float
    """
    return (a + b + c) / 3
    

def diferenca(a, b, c):
    """
    Essa função recebe os parâmetros a, b, c e retorna a diferença entre o maior deles e a média aritmética entre os 3;
    int, int, int -> float
    """
    return max(a, b, c) - media_3_inteiros(a, b, c)


def soma(a, b, c):
    """
    Essa função recebe os parâmetros a, b, c e retorna a soma entre o menor deles com a média aritmética entre os 3;
    int, int, int -> float
    """
    return min(a, b, c) + media_3_inteiros(a, b, c)


def discriminante(a, b, c):
    """
    Essa função recebe os coeficientes a, b, c de uma equação do segundo grau e calcula o discriminante;
    int, int, int -> int
    """
    return b ** 2 - 4 * a * c


def primeira_raiz_real(a, b, c):
    """
    Essa função recebe os coeficientes a, b, c de uma equação do segundo grau e calcula a primeira raiz real;
    int, int, int -> float
    """
    return (-b + math.sqrt(discriminante(a, b, c))) / 2 * a


def segunda_raiz_real(a, b, c):
    """
    Essa função recebe os coeficientes a, b, c de uma equação do segundo grau e calcula a segunda raiz real;
    int, int, int -> float
    """
    return (-b - math.sqrt(discriminante(a, b, c))) / 2 * a


def numero_de_termos(a1, an, r):
    """
    Essa função recebe o valor inicial(a1), final(an) e a razão(r) de uma Progressão Aritmética e calcula o número de termos;
    int, int, int -> float
    """
    return ((an - a1 + r) / r) / r


def soma_PA(a1, an, r):
    """
    Essa função recebe o valor inicial(a1), final(an) e a razão(r) de uma P.A. e calcula a soma dessa P.A.;
    int, int, int -> float
    """
    return ((an + a1) * numero_de_termos(a1, an, r)) / 2


def distancia(x1, y1, x2, y2):
    """
    Essa função recebe x1, y1 que configuram o ponto 1 no plano e x2, y2 que configuram o ponto 2 no plano. Então, a função calcula a distância entre esses pontos no plano;
    int, int, int, int -> float
    """
    return math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2)


def perimetro_triangulo_reto(c1, c2):
    """
    Essa função recebe o valor dos catetos de um triângulo retângulo e calcula seu perímetro;
    int, int -> float
    """
    return math.sqrt(c1 ** 2 + c2 ** 2) + c1 + c2


def soma_sin_cos(a):
    """
    Essa função recebe o valor do ângulo 'a' e retorna a soma do quadrado do seno com o quadrado do cosseno desse ângulo;
    int -> float
    """
    return math.sin(a) ** 2 + math.cos(a) ** 2


def area_setor_circular(r, a=1):
    """
    Essa função recebe o raio r da circunferência e o ângulo 'a' do setor circular e calcula a área do setor circular;
    int, int -> float
    """
    return (math.pi * (r ** 2) * a) / 360


def num_bombons(dinheiro, preco):
    """
    Essa função recebe o dinheiro que a pessoa tem e quanto custa cada bombom (preco). Ela calcula quantos bombons ele pode comprar; 
    int, int -> float
    """
    return dinheiro / preco


def carros(n_pessoas, capacidade=5):
    """
    Essa função recebe o número de pessoas (n_pessoas) que vão viajar e a capacidade do veículo, assim, ela calcula a quantidade de carros necessária para levar todas as pessoas;
    int, int -> float
    """
    return n_pessoas / capacidade


def bolos(A, B, C):
    """
    Essa função recebe os parâmetros A (quantidade de farinha), B (quantidade de ovos) e C (quantidade de sopas de leite), assim, retorna quantos bolos inteiros dá para fazer com esses ingredientes;
    int, int, int -> int
    """
    farinha = A / 2
    ovos = B / 3
    sopa_leite = C / 5
    divisor = 2
    mdc = 1
    while divisor <= farinha:
        if farinha % divisor == 0 and ovos % divisor == 0 and sopa_leite % divisor == 0:
            mdc = divisor
        divisor += 1
    return mdc


def mdc(a, b):
    divisor = 2
    mdc = 1
    while divisor <= a:
        if a % divisor == 0 and b % divisor == 0:
            mdc = divisor
        divisor += 1
    return mdc


print(mdc(45, 9))

