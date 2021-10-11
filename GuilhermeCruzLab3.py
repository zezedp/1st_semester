
def discriminante(a, b, c):
    """
    Essa função recebe os coeficientes a, b, c de uma equação do segundo grau e calcula o discriminante;
    int, int, int -> int
    """
    return b ** 2 - 4 * a * c

def quantidade_raizes(a, b, c):
    if discriminante > 0:
        return "duas"
    elif discriminante == 0:
        return "uma"
    else:
        return "nenhuma"

def mensagens_repetidas(texto, quantas_repeticoes):
    return texto * quantas_repeticoes


def data(dia, mes, ano):
    return f'{dia}/{mes}/{ano}'.format(str(dia), str(mes), str(ano))
