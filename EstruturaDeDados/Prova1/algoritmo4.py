"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada um dos identificadores (letras maiúsculas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    4) Escreva um teste sobre um vetor de 10 elementos para demonstrar a correção.
"""

"""
RESPOSTAS
1 = algoritimo Busca Binária
2 = a resposta esta em comentarios no meio do primeiro código
3 = o erro esta que esta comparando o elemento W com X
    CORREÇÃO = troquei o Y[W] pra Y[U]
"""

"""
# Z é o nome da função
# Y é a lista que vai ser feito a busca binária
# X é o elemento que vai ser buscado na lista=Y
def Z(Y, X):
    W = 0 # variavel de primeiro elemento            
    V = len(Y) - 1 # variavel do ultimo elemento 
    while W <= V:
        # U é a variavel do elemento médio
        U = (W + V) // 2
        if X == Y[W]: return U
        elif X < Y[W]: V = U - 1
        else: W = U + 1
    return -1
"""

def Zcorrigida(Y, X):
    W = 0                 
    V = len(Y) - 1    
    while W <= V:
        U = (W + V) // 2
        if X == Y[U]: return U
        elif X < Y[U]: V = U - 1
        else: W = U + 1
    return -1

lista_de_teste =[3, 5, 6, 2, 7, 8, 9, 4, 1, 10]

print('Lista desordenada: ')
print('Valor a ser buscado na lista é 3. ')
print(lista_de_teste)
Zcorrigida(lista_de_teste, 3)
print('Lista corrigida: ')
print(lista_de_teste)