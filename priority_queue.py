"""
o item removido da fila não é necessariamente o que foi incluído primeiro e,
sim, o que tem maior prioridade. Que prioridades são essas e como elas se
comparam umas com as outras não é especificado pela implementação Fila por
Prioridade. Isso depende de quais itens estão na fila.

Por exemplo, se os itens da fila tiverem nome, podemos escolhê-los por ordem
alfabética. Se for a pontuação de um jogo de boliche, podemos ir da maior 
para a menor, mas se for pontuação de golfe, teríamos que ir da menor para
a maior. Se é possível comparar os itens da fila, é possível achar e remover
o que tem maior prioridade. Essa implementação da Fila por Prioridade tem 
como atributo uma lista Python chamada items, que contém os itens da fila.
"""


class Item():
    def __init__(self, label: str, priority: int):
        self._label = label
        self._priority = priority

    @property
    def label(self):
        return self._label

    @property
    def priority(self):
        return self._priority

    def __lt__(self, o: object) -> bool:
        return self.priority < o.priority

    def __le__(self, o: object) -> bool:
        return self.priority <= o.priority

    def __eq__(self, o: object) -> bool:
        return self.priority == o.priority

    def __ne__(self, o: object) -> bool:
        return self.priority != o.priority

    def __gt__(self, o: object) -> bool:
        return self.priority > o.priority

    def __ge__(self, o: object) -> bool:
        return self.priority >= o.priority

    def __str__(self):
        return self._label + ", " + str(self.priority)


class PriorityQueue():

    def __init__(self):
        self._pq = []
        self._len = 0

    @property
    def pq(self):
        return self._pq

    @property
    def len(self):
        return self._len

    def isEmpty(self):
        if self._len == 0:
            return True
        return False

    def addOne(self):
        self._len += 1

    def delOne(self):
        self._len -= 1

    def __str__(self):
        for i in self.pq:
            print(i)
        return "\n"

    # inserts on a priority decreasingly ordered fashion
    def push(self, item):
        # error first
        if not isinstance(item, Item):
            print(f"To insert {item} must be an instance of Item Class")
        else:
            if self.isEmpty():
                self.pq.append(item)
                self.addOne()
            else:

                flag_push = False

                # search for the right priority
                for index in range(self.len):
                    if self.pq[index] <= item:
                        self._pq.insert(index, item)
                        flag_push = True
                        break

                if not flag_push:
                    self._pq.append(item)

                self.addOne()

    def pop(self):
        self._pq.pop()
        self.delOne()
