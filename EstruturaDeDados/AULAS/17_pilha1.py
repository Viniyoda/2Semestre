"""
Programa simples que inverte uma palavra informada pelo usuário
e verifica se ela é um PALÍNDROMO, isto é, uma palavra que pode
ser lida tanto da frente para trás quanto de trás para frente.
Para isso, usaremos uma estrutura de pilha baseada em uma lista
do Python.
"""
palavra = input("Informe a palavra a ser verificada: ")

# Lista vazia que será usada como pilha
pilha = []

# 1) Pega cada letra da palavra (convertida em maiúsculas,
#    para facilitar a posterior comparação) e insere no
#    final (topo) da pilha
for letra in palavra.upper():
    pilha.append(letra)
    print(pilha)

print("-" * 50)

# 2) Vamos retirar cada uma das letras da pilha, DO FIM PARA O INÍCIO.
#    A operação se repete enquanto a pilha não estiver vazia (len > 0).
#    Cada letra retirada é acrescentada à variável "inverso".
inverso = ""

while len(pilha) > 0:
    letra = pilha.pop()
    inverso += letra
    print(f"Pilha: {pilha}, inverso: {inverso}")

print("-" * 50)

print("Palavra original: ", palavra.upper())
print("Palavra invertida:", inverso)

# Verifica se é palíndromo
if palavra.upper() == inverso:
    print("*** É UM PALÍNDROMO **")
else:
    print("-- não é um palíndromo --")