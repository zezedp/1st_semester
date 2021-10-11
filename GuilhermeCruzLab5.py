def contato_novo(nome, telefone = '', email = '', instagram = ''):
    '''
    Essa função recebe o nome, telefone, email e instagram de 
    um usuário e retorna esses valores em uma lista;
    str, str, str, str -> list
    '''
    return [nome, list(telefone), email, instagram]
    



def atualizar_contato(contato_novo, indice, nova_informacao):
    '''
    Essa função recebe a função anteriormente elaborada "contato_novo", 
    o indice da lista retornada pela função "contato_novo" e a informação que 
    o usuário quer usar agora. Assim, ela retorna se alterou a lista ou não;
    
    list, int, str -> bool
    
    '''
    if indice == 0:
        contato_novo[0] = nova_informacao
    elif indice == 1:
        if nova_informacao == contato_novo[1]:
            return False
        contato_novo[1] += nova_informacao
    elif indice == 2:
        contato_novo[2] = nova_informacao
    elif indice == 3:
        contato_novo[3] = nova_informacao
    elif indice > 3:
        return False
    return True
        

def aminoacidos(rna_mensageiro):
    '''
    Essa função recebe o rna_mensageiro e retorna os aminoacidos 
    correspondentes a cada trinca;
    str -> str
    '''
    mapeamento_rna_aminoacido = {
        'UUU': 'Phe',
        'CUU': 'Leu',
        'UUA': 'Leu',
        'AAG': 'Lisina',
        'UCU': 'Ser',
        'UAU': 'Tyr',
        'CAA': 'Gln'
    }
    resultado = ''
    j = 3
    trincas = [rna_mensageiro[i:i+j] for i in range(0, len(rna_mensageiro), j)]
    for n in trincas:
        resultado += mapeamento_rna_aminoacido[n]
        resultado += '-'

    return resultado[:len(resultado)-1]
