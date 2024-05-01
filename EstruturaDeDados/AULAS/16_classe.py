"""
Classe é uma estrutura que representa conjuntamente dados e
algoritmos. Uma classe pode ser comparada a uma "assadeira",
com a qual se pode produzir diferentes tipos de "assados"
(objetos), variando os "ingredientes" (dados) e o "modo de
fazer" (algoritmos). Apesar dessas variações, todos os objetos
criados a partir de uma mesma classe terão sempre algumas
características comuns impostas por esta.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classes seguem o formato PascalCase
    (primeira letra de cada palavra em maiúsculo).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, representando os algoritmos). Uma função especial,
    chamada __init__, é chamada sempre que se tenta criar um novo
    objeto a partir de uma classe. Essa função especial é chamada
    de CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS; seu primeiro parâmetro
       é sempre self, o qual representa o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        """ Método construtor """
        self.set_base(base)
        self.set_altura(altura)
        self.set_tipo(tipo)

    def set_base(self, val):
        """
        Método setter para o atributo __base
        """
        if type(val) not in [int, float] or val <= 0:
            raise Exception("ERRO: o parâmetro 'base' deve ser numérico e maior que zero.")
        self.__base = val

    def set_altura(self, val):
        """
        Método setter para o atributo __altura
        """
        if type(val) not in [int, float] or val <= 0:
            raise Exception("ERRO: o parâmetro 'altura' deve ser numérico e maior que zero.")
        self.__altura = val

    def set_tipo(self, val):
        """
        Método setter para o atributo __tipo
        """
        if val not in ["R", "T", "E"]:
            raise Exception("ERRO: o parâmetro 'tipo' deve ter um dos seguintes valores: 'R', 'T' ou 'E'.")
        self.__tipo = val

    def get_base(self):
        """
        Método getter para o atributo __base
        """
        return self.__base
    
    def get_altura(self):
        """
        Método getter para o atributo __altura
        """
        return self.__altura
    
    def get_tipo(self):
        """
        Método getter para o atributo __tipo
        """
        return self.__tipo
    
    def calc_area(self):
        """
        Método que calcula a área da forma, com base nos valores de
        __base, __altura e __tipo
        """
        if self.__tipo == "R":      # Retângulo
            return self.__base * self.__altura
        if self.__tipo == "T":      # Triângulo
            return self.__base * self.__altura / 2
        else:                       # Elipse/círculo
            return (self.__base / 2) * (self.__altura / 2) * pi

    def __str__(self):
        """
        Retorna uma representação dos valores armazenados dentro do objeto
        como uma string, para que possamos visualizá-los
        """
        return f"[OBJETO] base: {self.__base}, altura: {self.__altura}, tipo: {self.__tipo}"

#############################################################################
        
forma1 = FormaGeometrica(10, 13, "R")
forma2 = FormaGeometrica(7.5, 8.2, "T")

#forma1.base = "batata"
#forma1.set_base("batata")
forma1.set_base(12)
#forma1.altura = -3
forma1.set_altura(3)
#forma1.tipo = "K"
forma1.set_tipo("E")

print(forma1)
print(forma2)

print('-' * 60)

#print(f"Base de forma1: {forma1.__base}")
print(f"Base de forma1: {forma1.get_base()}")
print(f"Altura de forma1: {forma1.get_altura()}")
print(f"Tipo de forma1: {forma1.get_tipo()}")
print(f"Área de forma1: {forma1.calc_area()}")

print('-' * 60)

print(f"Base de forma2: {forma2.get_base()}")
print(f"Altura de forma2: {forma2.get_altura()}")
print(f"Tipo de forma2: {forma2.get_tipo()}")
print(f"Área de forma2: {forma2.calc_area()}")