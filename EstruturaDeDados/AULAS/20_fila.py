from lib.queue import Queue

# Inicializa uma fila
fila_ubs = Queue()

# Insere algumas pessoas na fila
fila_ubs.enqueue("Leonilda")
fila_ubs.enqueue("Otacílio")
fila_ubs.enqueue("Waldisney")
fila_ubs.enqueue("Adamastor")

print(fila_ubs)

# Atende uma pessoa
atendido = fila_ubs.dequeue()
print(f"Foi atendido(a): {atendido}")
print(fila_ubs)

# Mais duas pessoas chegaram
fila_ubs.enqueue("Margarete")
fila_ubs.enqueue("Gervásio")
print("Duas novas pessoas:", fila_ubs)

# Mais um paciente foi chamado para atendimento
atendido = fila_ubs.dequeue()
print(f"Foi atendido(a): {atendido}")
print(fila_ubs)
