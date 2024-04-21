"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada um dos identificadores (letras maiúsculas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    4) Escreva um teste sobre um vetor de 10 elementos para demonstrar a correção.
"""

"""
RESPOSTAS
1 = algoritimo de Quick Sort
2 = a resposta esta em comentarios no meio do primeiro código
3 = o erro esta na chamada 'Z(Y, U, W - 1)', se o pivo for o ultimo elemento
    isso vai dar um intervalo com valor negativo que esta errado
    CORREÇÃO = para arrumar alterei a condição da chamada pra 'W'
"""

"""
# Z é o nome da função
# Y é a lista que vai ser ordenada
# X é o elemento inicial da lista que é 0
# W é o elemento final da lista que é None
def Z(Y, X = 0, W = None):
    if W is None: W = len(Y) - 1
    if W <= X: return
    V = W # é o elemento do pivo
    U = X - 1 # é o indicador de menor elemento
    for T in range(X, W):
        if Y[T] < Y[V]:
            U += 1
            if(T != U):
                Y[T], Y[U] = Y[U], Y[T]
                # a linha acima faz as trocas dos elementos menores que o pivo pra a esquerda
    U += 1
    if(U != V):
        Y[U], Y[V] = Y[V], Y[U] # coloca pivo  como posição final
    Z(Y, X + 1, U) # chama a def para parte esquerda da lista
    Z(Y, U, W - 1) # chama a def para parte direita da lista
"""

def Zcorrigida(Y, X=0, W=None):
    if W is None:
        W = len(Y) - 1
    if W <= X:
        return
    V = W
    U = X - 1
    for T in range(X, W):
        if Y[T] < Y[V]:
            U += 1
            if T != U:
                Y[T], Y[U] = Y[U], Y[T]
    U += 1
    if U != V:
        Y[U], Y[V] = Y[V], Y[U]
    Zcorrigida(Y, X, U - 1)
    Zcorrigida(Y, U + 1, W)

lista_de_teste =[3, 5, 6, 2, 7, 8, 9, 4, 1, 10]

print('Lista desordenada: ')
print(lista_de_teste)
Zcorrigida(lista_de_teste)
print('Lista corrigida: ')
print(lista_de_teste)