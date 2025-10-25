def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    while tamanho > 0:
        posicao.append([linha, coluna])
        tamanho -= 1

        if orientacao == 'vertical':
            linha += 1
        if orientacao == 'horizontal':
            coluna += 1
    return posicao

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in frota:
        frota[navio].append(posicao)
    else:
        frota[navio] = [posicao]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for lista_de_navios in frota.values():
        for navio in lista_de_navios:
            for linha, coluna in navio:
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    afundados = 0

    for lista_de_navios in frota.values():
        for navio in lista_de_navios:
            afundado = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                afundados += 1

    return afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicao_novo = define_posicoes(linha, coluna, orientacao, tamanho)
    for linha, coluna in posicao_novo:
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False
    for lista_de_navios in frota.values():
        for navios in lista_de_navios:
            for posicao in navios:
                if posicao in posicao_novo:
                    return False
    return True