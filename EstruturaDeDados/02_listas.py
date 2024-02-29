#Listas são uma estrutura de dados nativas da
# LINGUAGEM PYTHON. Elas permitem que varios.
# Valores possam ser associados a uma unica variavel

# Listas de strings
legumes = ['Batata','cenoura','beterraba','mandioca','batata doce',]

#Listas de numeros
nums = [3,10,-7,12.8,-0.5]

#Listas com valores de varios tipos

Mistureba = ['Joaquim', 37, 1.81,88,True]

#   1) Percuso
# Percorrer uma lista significa visitar cada um de seus itens e fazer algo com ele.
# No exemplo abaixo vamos dar print em cada um dos legumes da lista

for leg in legumes:
    print(leg)

#separador  
print ('-'*60 )  

# Percorrendo lista de numeros e printando o valor do dobor de cada item
for n in nums:
    print(n * 2)

#separador  
print ('-'*60 )  
 # 2) Inserção  de um novo elemento no *Fim  da lista* append()

nums.append(6)
legumes.append('mandioca')

print(nums)
print(legumes)

#separador  
print ('-'*60 )

# 3) inserção de um novo elemento na posição especificada: insert()
# parametros:
# 1 - a posição onde sera feita a inserção
# 2 - o novo elemento a ser inserido

# inserindo um novo elemento na quarta posição
legumes.insert(3, "tomate")
print(legumes)

# inserindo um novo lemento na primeira posição
legumes.insert(0, "milho")
print(legumes)

# traço separador
print("-" * 60)

# 4) acessando valores, informando a respectiva posição
print("Elemento na QUINTA posição:", legumes[4])
print("Elemento na PRIMEIRA posição:", legumes[0])
print("Elemento na ÚLTIMA posição:", legumes[-1])
print("Elemento na PENÚLTIMA posição:", legumes[-2])

# traço separador
print("-" * 60)

# 5) substituindo valores existentes

print("ANTES", legumes)

# substituindo o valor na posição 3 (quarta posição)
legumes[3] = "vagem"
# substituindo o valor na posição 0 (primeira posição)
legumes[0] = "nabo"
# substituindo o valor na posição -1 (última posição)
legumes[-1] = " inhame"

print("DEPOIS", legumes)

# traço separador
print("-" * 60)

# 6) determinando a quantiade de elementos da lista: len()
print("Quantidade de elementos da lista de legumes:", len(legumes))
print("Quantidade de elementos da lista de números:", len(nums))

# traço separador
print("-" * 60)

# 7) removendo o último elemento de uma lista: pop() (sem parâmetro)
print("ANTES", legumes)
removido = legumes.pop()
print("Valor removido", removido)
print("DEPOIS", legumes)

# traço separador
print("-" * 60)

# 8) removendo um elemento por us posição: pop() (com parâmetro)
print("Antes", legumes)
removido = legumes.pop(3)       # remove o elemento da posição 3
print("Valor removido da posição 3:", removido)

removido = legumes.pop(0)       # remove o primeiro elemento
print("Valor removido da primeira posição:", removido)
print("DEPOIS", legumes)

# traço separador
print("-" * 60)

# 9) removendo um elemento por seu valor: remove()
legumes.append("mandioquinha")
legumes.remove("mandioquinha")
print(legumes)

# traço separador
print("-" * 60)

# 10) juntando (concatenado) duas listas: extend()
mais_legumes = ["abobrinha", "quiabo", "jiló", "cambotiá", "cará"]
legumes.extend(mais_legumes)
print(legumes)

# traço separador
print("-" * 60)

# 11) fatiando uma lista
#     fatiar siginifica copiar um pedaço da lista (uma sublista)
#     para uma nova lista

# cria uma sublista que contém os elementos das posições 2 a 5
# (posição 6 não entra)
sublista2_5 = legumes[2:6]
print("Sublista de 2 a 5:", sublista2_5)

# cria uma sublista que contpem os elementos desde o inpicio a até a posição 6 (posição 7 não entra)
sublista_inicio_6 = legumes [:7]
print("Sublista do inpicio até a posição 6:", sublista_inicio_6)

# cria uma sublista que contém os elementos da posição 4 até o final
sublista_4_fim = legumes[4:]
print("Sublista da posição 4 até o final:", sublista_4_fim)

# traço separador
print("-" * 60)




