"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada um dos identificadores (letras maiúsculas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    4) Escreva um teste sobre um vetor de 10 elementos para demonstrar a correção.
"""

"""
RESPOSTAS
1 = algoritimo selection sort
2 = a resposta esta em comentarios no meio do primeiro código
3 = o erro esta na ultima linha do código onde deixei como comentário '#',
    ja que quando o if é verdadeiro o valor de 'V' não é conhecido ja que foi declarado só no for
    CORREÇÃO = arrumei a linha de troca dos elementos no array
"""

"""
# A variavel Y é a lista que vai ser ordenada
# A letra Z é o nome da função
def Z(Y):
    # A letra X é usado para percorrer a lista, como o for i
    for X in range(len(Y) - 1):
        # O W é utilizado pra encontrar o menor elemento da lista não ordenada
        W = X + 1
        # O V é como o X, utilizado pra percorrer a lista mas nesse caso não ordenada
        for V in range(W + 1, len(Y)):
            if Y[V] < Y[W]: W = V
        if Y[W] < Y[X]: 
        #    Y[V], Y[X] = Y[X], Y[V]
"""

def Zcorrigida(Y):
    for X in range(len(Y) - 1):
        W = X
        for V in range(W + 1, len(Y)):
            if Y[V] < Y[W]: W = V
        if Y[W] < Y[X]: 
            Y[W], Y[X] = Y[X], Y[W]

lista_de_teste =[3, 5, 6, 2, 7, 8, 9, 4, 1, 10]

print('Lista desordenada: ')
print(lista_de_teste)
Zcorrigida(lista_de_teste)
print('Lista corrigida: ')
print(lista_de_teste)
