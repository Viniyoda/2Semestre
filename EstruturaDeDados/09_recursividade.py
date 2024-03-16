def fatorial_iter(num):
    """
    Calcula o fatorial de um npumero usando um algoritimo
    ITERATIVO (não recursivo)
    """

    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")

    resposta = 1
    for n in range(num, 0, -1): resposta *= n

    return resposta

print("Fatorial de 5:(iterativa)", fatorial_iter(5))
print("Fatorial de 8:(iterativa)", fatorial_iter(8))

####################################################################

def fatorial_rec(num) :
    """
    Cálculo do fatorial, usando um algoritmo RECURSIVO
    """

    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")

    if num <= 1: return 1       # O fatorial de 0 e 1 é igual a 1
    else: return num * fatorial_rec(num - 1)    # Chamada recursiva

####################################################################

print("Fatorial de 5:(recursivo)", fatorial_rec(5))
print("Fatorial de 8:(recursivo)", fatorial_rec(8))