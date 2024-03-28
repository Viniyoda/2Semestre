#Crie um novo arquivo chamado atividade1.py.
#Declare uma lista contendo os seguintes carros: Fusca, Chevette, Opala, Maverick e Fiorino.
#Pesquise como se faz em Python e implemente as seguintes alterações:
#Insira o carro Brasília no final da lista.
#Insira o carro Alfa Romeo no início da lista.
#Insira o carro Corcel na lista entre os carros Chevette e Opala.
#Remova o carro Maverick da lista.
#Envie o arquivo atividade1.py até o prazo final.

carros = ['Fusca', 'Chevette', 'Opala', 'Maverick', 'Fiorino']
print(carros)
carros.append('Brasília')
print(carros)
carros.insert(0, 'Alfa Romeo')
print(carros)
carros.insert(3, 'Corcel')
print(carros)
carros.remove('Maverick')
print(carros)