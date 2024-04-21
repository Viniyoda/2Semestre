"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada um dos identificadores (letras maiúsculas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    4) Escreva um teste sobre um vetor de 10 elementos para demonstrar a correção.
"""

"""
RESPOSTAS
1 = algoritimo Bubble Sort
2 = a resposta esta em comentarios no meio do primeiro código
3 = o erro esta na identação do if not X, ja que ele esta dentro do for e ele deveria estar fora
    pra verificar só uma vez o loop
    CORREÇÃO = apenas retirei o if de dentro do for
"""

"""
# Z é o nome da função
# Y é a lista que vai ser ordenada
def Z(Y):
    while 1 > 0:
        # X é a variavel boolean pra sinalizar se trocas
        X = False
        # a letra W é usada pra percorrer a lista
        for W in range(len(Y) - 1):
            if Y[W + 1] < Y[W]:
                Y[W + 1], Y[W] = Y[W], Y[W + 1]
                X = True
            if not X:
                break
"""

def Zcorrigida(Y):
    while 1 > 0:
        X = False
        for W in range(len(Y) - 1):
            if Y[W + 1] < Y[W]:
                Y[W + 1], Y[W] = Y[W], Y[W + 1]
                X = True
        if not X:
            break

lista_de_teste =[3, 5, 6, 2, 7, 8, 9, 4, 1, 10]

print('Lista desordenada: ')
print(lista_de_teste)
Zcorrigida(lista_de_teste)
print('Lista corrigida: ')
print(lista_de_teste)
