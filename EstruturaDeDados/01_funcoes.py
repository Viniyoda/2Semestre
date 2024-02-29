def imc(peso, altura):
   resultado = peso / altura ** 2
   return resultado

print(f'O imc de uma pessoa com 78 kilos e 1 metro e 83 cm, é  {imc(78,1.83) }')

#################################################################

from math import pi

def calc_area(base,altura,tipo):
    if tipo == 'R':    #Retangulo
        return  base * altura
    elif tipo == 'T':    #Triangulo
        return base * altura / 2
    elif tipo == 'E':   #Elipse
        return (base / 2) * (altura / 2) * pi
    else:
        return None
print(f'Area do rentagulo 22x47: {calc_area(22,47, 'R')}')

print(f'Area do triangulo 10x13: {calc_area(10,13, 'T')}')

print(f'Area da elipse 8x20: {calc_area(8,20, 'E')}')

print(f'Area do invalida 10x13: {calc_area(8,11.5, 'W')}')
        