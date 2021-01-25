"""

    São estruturas de dados do tipo FIFO (first-in first-out), 
onde o primeiro elemento a ser inserido, será o primeiro a ser
retirado, ou seja, adiciona-se itens no fim e remove-se do início.

São exemplos de uso de fila em um sistema:

    Controle de documentos para impressão;
    Troca de mensagem entre computadores numa rede;
    etc. 

    A implementação de filas pode ser realizada através de vetor 
(alocação do espaço de memória para os elementos é contígua) ou
através de listas encadeadas (próxima aula).

Operações com Fila:

    Todas as operações em uma fila podem ser imaginadas como as 
que ocorre numa fila de pessoas num banco, exceto que o elementos
não se movem na fila, conforme o primeiro elemento é retirado. 
Isto seria muito custoso para o computador. O que se faz na realidade
é indicar quem é o primeiro.

   ' criação da fila (informar a capacidade no caso de implementação sequencial - vetor);
   ' enfileirar (enqueue) - o elemento é o parâmetro nesta operação;
   ' desenfileirar (dequeue);
   ' mostrar a fila (todos os elementos);
   ' verificar se a fila está vazia (isEmpty);
   ' verificar se a fila está cheia (isFull - implementação sequencial - vetor). 
"""


class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, el):
        self.len_queue += 1
        self.queue.append(el)

    def pop(self):
        if not self.is_empty():
            self.queue.pop(0)

    def is_empty(self):
        if self.len_queue != 0:
            return False
        return True

    def lenght(self):
        return self.len_queue

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def back(self):
        if not self.is_empty():
            return self.queue[-1]
        return None

    def __str__(self) -> str:
        string = ''
        if not self.is_empty():
            for i in self.queue:
                string += str(i) + "\n"
        return string


q = Queue()
print(q)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q)
q.pop()
q.push(5)
print(q)
q.pop()
print(q)
