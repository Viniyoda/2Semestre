
frutas = ['laranja', 'maca', 'uva', 'pera', 'mamao', 'abacate', 'amora']

# para percorrer uma lista e exibir apenas seus elementos,
# usamos a estrutura for..in, como ja visto no aquivo n-2

for f in frutas:
    print(f)

print("-"*60)

# percorrendo uma lista em ordem inversa: reversed()

for x in reversed(frutas):
    print(x)

print("-"*60)

# no entanto, frequentemente precisamos exibir, além do
# valor do elemento, também sua posição. nesse caso, devemos
# usar a função for..in combinado com as funções range() e len()

for pos in range(len(frutas)):
    print(pos, ':', frutas[pos])

print("-"*60)

# as vezes é necessario percorrer a lista de trás para frente,
# mas tendo acesso também a posição dos elementos. para isso,
# usamos a estrutura for..in, len() e range() com três parâmetros

for i in range(len(frutas) -1, -1, -1):
    print(i, ':', frutas[1])
