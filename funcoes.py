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