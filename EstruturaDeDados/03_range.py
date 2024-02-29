# range() é uma função que gera uma faixa de números.
# é muito usado em associação com listas

# 1) range() com *um* parâmetro
#    gera uma faixa numérica que vai de 0 até o valor
#    do parâmetro - 1
for num in range(10):
    print(num)

# traço separador
print("-" * 60)

# 2) range() com *dois* parâmetros
#    1 - parâmetro > valor inicial da faixa
#    2 - parâmetro > valor final da faixa (não incluído)
for x in range(10, 16):
    print(x)

# traço separador
print("-" * 60)

# 3) range() com *três* parâmetros
#    1 - parâmetro > valor inicial da faixa
#    2 - parâmetro > valor final da faixa (não incluído)
#    3 - parâmetro > passo (intervalo entre um número e outro)
for n in range(1, 22, 3):   # de 1 a 21 contando de 3 em 3
    print(n)

# traço separador
print("-" * 60)

# range() com passo negativo
for i in range(10, 0, -1):   # contagem regressiva de 10 a 1
    print(i)

    # traço separador
print("-" * 60)




