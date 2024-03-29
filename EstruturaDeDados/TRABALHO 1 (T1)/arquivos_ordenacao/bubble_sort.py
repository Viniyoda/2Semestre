# Variáveis de contagem
comps = trocas = passd = 0

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR do que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última passada,
    nenhuma troca tenha sido efetuada.    
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop eterno; não sabemos antecipadamente quantas passadas
    # serão necessárias
    while True:

        passd += 1

        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        for pos in range(len(lista) - 1):

            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # efetuamos uma TROCA
            if lista[pos + 1] < lista[pos]:
                # Troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True   # Houve troca na passada

            comps += 1

        print(lista)

        # Se não houve trocas na passada, a lista está ordenada
        # e interrompemos o loop eterno while True
        # <~ CUIDADO COM A INDENTAÇÃO
        if not trocou:
            break

#########################################################################

import sys, tracemalloc
sys.dont_write_bytecode = True  # Impede a criação do cache
from time import time

#########################################################################

# Importando a lista de empresas
from data.emp10mil import empresas
#from data.emp25mil import empresas
#from data.emp50mil import empresas
#from data.emp100mil import empresas

#########################################################################

tracemalloc.start()         # Inicia medição do consumo de memória
hora_ini = time()
bubble_sort(empresas)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()          # Termina a medição de memória

#########################################################################

print(empresas)    # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparacoes: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")
