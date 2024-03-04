def busca_binaria(lista, val):
    """"
    algoritimo de busca binaria
    dados uma lista, que deve estar previamente ordenada,
    e um valor de busca, divide a lista em duas partes,
    procurando pelo valor de busca apenas na metade onde
    o valor de busca poderia estar. novas subdivisões ou que
    reste apenas uma sublista vazia, quando estão se
    conclui que o valor de busca não existe na lista
    """

    # declaramos que queremos usar a variavel global comps
    # inicializando na linha 1

    global comps
    comps = 0

    ini = 0                 # posição inicial da lista
    fim = len(lista) - 1    # pisução final da lista

    while ini <= fim:
        # calculando o meio da lista
        meio = (ini +fim) // 2      # DIVISÃO INTEIRA ( // )

        # verifica se o valor que está no meio da lista
        # é igual ao valor de busca. em caso afirmativo,
        # retornamos a posição do meio, pois o valor de
        # busca foi encontrado
        
        if val == lista[meio]:
            comps += 1
            return meio
        
        # senão, se o valor de busca é menor do que o
        # valor do meio, reinicia a busca na metade esquerda
        # da (sub)lista

        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        # por fim, se o valor e busca é MAIOR do que o
        # valor do meio, reinicia a busca na metade direita
        # do (sub)lista
            
        else:
            comps += 2
            ini = meio + 1

    # <- CUIDADO COM A IDENTAÇÃO AQUI!
    # se chegarmos a este ponto, é porque o valor de busca não
    # existe na lista
    return -1

########################################################################

import sys
sys.dont_write_bytecode = True

from time import time

from data.nomes_completos import nomes

hora_ini = time()
resultado1 = busca_binaria(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posicao {resultado1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")
print(f"Comparacoes: {comps}")

hora_ini = time()
resultado2 = busca_binaria(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERREIRA encontrado na posicao {resultado2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")
print(f"Comparacoes: {comps}")

hora_ini = time()
resultado3 = busca_binaria(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encontrado na posicao {resultado3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")
print(f"Comparacoes: {comps}")

hora_ini = time()
resultado4 = busca_binaria(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontrado na posicao {resultado4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")
print(f"Comparacoes: {comps}")