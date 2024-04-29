class DoublyLinkedList:
    """
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos
    (chamados nodos ou nós) não estão fisicamente adjacentes
    uns dos outros, mas ligados de forma lógica por ponteiros
    que indicam o nodo anterior e o nodo seguinte da
    sequência. Não possui restrições de acesso - inserções,
    exclusões e consultas podem ser executadas em qualquer
    posição da lista
    """
    #---------------------------------------------------------
    class Node:
        """
        Classe interna que representa a unidade de informação
        (nodo) armazenado pela lista duplamente encadeada
        """
        def __init__(self, data):
            """ Construtor da classe interna """
            self.prev = None  # Ponteiro para o nodo anterior
            self.data = data  # Dado útil para usuário
            self.next = None  # Ponteiro para o nodo seguinte
    #---------------------------------------------------------

    def __init__(self):
        """
        Construtor da classe principal DoublyLinkedList
        """
        self.__head = None  # Ponteiro para o primeiro nodo
        self.__tail = None  # Ponteiro para o último nodo
        self.__count = 0    # Quantidade de nodos na lista

    def __find_node(self, pos):
        """
        Método PRIVADO que encontra um nodo na posição
        especificada
        """
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.__count - 1),
        # retorna self.__tail
        if pos == self.__count - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se a posição estiver na primeira metade da lista,
        # faz o percurso a partir de self.__head, seguindo
        # o ponteiro next
        if pos < self.__count // 2:
            # Percorre a lista quantas vezes forem necessárias
            # até encontrar o nodo da posição desejada
            node = self.__head
            for _ in range(1, pos + 1): node = node.next
            return node
        
        # Senão, a posição estando na segunda metade da lista,
        # faz o percurso reverso a partir de self.__tail,
        # seguindo o ponteiro prev
        else:
            node = self.__tail
            for _ in range(self.__count - 2, pos - 1, -1):
                node = node.prev
            return node

    def insert(self, pos, val):
        """
            Método que insere na posição 'pos' o valor 'val
        """

        # Criamos um novo nodo para armazenar "val" e também
        # os ponteiros "prev" e "next", ambos apontando
        # inicialmente para None
        new = self.Node(val)

        # 1º caso: a lista está vazia, e "new" será, ao mesmo
        # tempo, tanto o primeiro quanto o último nodo
        if self.__count == 0:
            self.__head = new
            self.__tail = new

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new

        # 3º caso: inserção no final da lista
        # OBS.: consideramos como posição final da lista
        # qualquer uma que seja >= self.__count
        elif pos >= self.__count:
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4º caso: inserção em posição intermediária
        # Não temos acesso direto às posições intermediárias.
        # Para encontrá-la, precisaremos partir de uma das
        # extremidades (__head ou __tail) e percorrer a lista
        # até encontrar o nodo que, atualmente, ocupa a
        # posição onde o novo será inserido. Essa busca será
        # feita por um outro método, chamado __find_node()
        else:
            # Busca o nodo que atualmente ocupa a posição de 
            # inserção
            current = self.__find_node(pos)

            # Determina o nodo anterior à posição
            before = current.prev

            # Efetua o encaixe do novo nodo na sequência
            before.next = new
            new.prev = before
            new.next = current
            current.prev = new

        # Incrementa a quantidade de elementos da lista
        # após uma inserção em qualquer caso
        self.__count += 1