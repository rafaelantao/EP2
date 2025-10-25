from funcoes import *

frotainfos = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
} 

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for navio in frota:
    tamanho = frotainfos[navio][0]
    qtd = frotainfos[navio][1]
    for i in range (qtd):
        posicaovalida = False
        while not posicaovalida:
            print('Insira as informações referentes ao navio {} que possui tamanho {}'.format(navio, tamanho))
            linha = input(int('Linha:'))
            coluna = input(int('Coluna:'))
            orientacao = 'vertical'
            if navio != 'submarino':
                orientacao = input(int('[1] Vertical [2] Horizontal >'))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            posicaovalida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
        posicao = define_posicoes(linha, coluna, orientacao, tamanho)
        frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)