class Deque:
    """
    ESTRUTURA DE DADOS DEQUE
    Deque (Double-Ended QUEue) é uma estrutura de dados derivada
    da fila, que permite inserções e remoções em qualquer uma de
    suas extremidades. Com isso, o deque pode se comportar tanto
    como uma fila comum quanto como uma fila em que são admitidas
    inserções prioritárias (na primeira posição) quanto a possi-
    bilidade de remoção do último item (desistência).
    """
    def __init__(self):
        """ Método construtor """
        self.__data = []    # Lista vazia

    def insert_front(self, val):
        """ Método para inserção no início (posição 0) """
        self.__data.insert(0, val)

    def insert_back(self, val):
        """ Método para inserção no final """
        self.__data.append(val)

    def is_empty(self):
        """ Retorna se o deque está ou não vazio """
        return len(self.__data) == 0
    
    def remove_front(self):
        """ Método de remoção na posição inicial """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio.")
        return self.__data.pop(0)
    
    def remove_back(self):
        """ Método de remoção na posição final """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio.")
        return self.__data.pop()
    
    def peek(self, front = True):
        """
        Método que consulta um elemento do deque sem removê-lo.
        Se o parâmetro 'front' for True (ou tiver sido omitido),
        será retornado o primeiro elemento.
        Caso contrário, será retornado o último elemento.
        """
        if front: return self.__data[0]     # Primeiro elemento
        else: return self.__data[-1]        # Último elemento

    def __str__(self):
        """ Retorna uma representação do deque como string """
        return str(self.__data)