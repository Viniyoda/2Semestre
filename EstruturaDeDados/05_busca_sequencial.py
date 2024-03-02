
def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista,
    procurando por val.
    se val for encontrado, retorna a posição de val na lista.
    caso contrário, retorna o valor convencional -1.
    """
    # percorre a lista do inicio ao fim usando range() e len()
    # é necessário ter acesso ás posições dos elementos

    for pos in range(len(lista)):
        #encontrou val: retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # <-- CUIDADO COM A IDENTAÇÃO AQUI!
    # percorreu toda a lista e não encontrou val: retorna -1
    return -1

##############################################################################

# lista de números para testar

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

# TESTES

pos30 = busca_sequencial(nums,30)
print(f"Elemento 30 encontrado na posicao {pos30}")

pos_menos15 = busca_sequencial(nums,-15)
print(f"Elemento -15 encontrado na posicao {pos_menos15}")

pos19 = busca_sequencial(nums,19)
print(f"Elemento 19 encontrado na posicao {pos19}")

print("-"*60)

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True

from time import time

from data.nomes_completos import nomes

hora_ini = time()
resultado1 = busca_sequencial(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posicao {resultado1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")

hora_ini = time()
resultado2 = busca_sequencial(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERREIRA encontrado na posicao {resultado2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")

hora_ini = time()
resultado3 = busca_sequencial(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encontrado na posicao {resultado3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")

hora_ini = time()
resultado4 = busca_sequencial(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontrado na posicao {resultado4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms/n")