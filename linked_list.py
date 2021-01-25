"""
Listas encadeadas são a forma mais simples de estrutura de dados 
dinâmica. Em uma lista, os elementos não são armazenados contigu-
amente, como acontece em arranjos. Nelas, cada elemento é armaze-
nado separadamente, e possui valor (o dado que desejamos acessar)
e um ponteiro para o próximo elemento. Um ponteiro (ou apontador)
é uma variável que armazena o endereço de outra variável (eles 
referenciam outra variável). No caso de listas encadeadas, um 
ponteiro armazena o endereço do próximo elemento da lista. Para
percorrermos a lista, basta seguirmos os ponteiros ao longo dela.
"""


class Node():

    def __init__(self, label):
        self._label = label
        self._next = None

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label = label

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    def __str__(self):
        return f"Node {self._label} --> {self._next.get_label() if self._next else 'Linked list ending'}"


class LinkedList():

    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    def push(self, label, index=0):

        if index >= 0:
            # create a new Node
            node = Node(label)

            if self.isEmpty():
                self._first = node
                self._last = node

            else:
                # push at first position
                if index == 0:
                    node.set_next(self._first)
                    self._first = node
                # Push last position
                elif index >= self._length:
                    self._last.set_next(node)
                    self._last = node
                else:
                    # push in the middle

                    prev_node = self._first
                    curr_node = self._first.get_next()
                    curr_index = 1

                    while curr_node != None:
                        if curr_index == index:
                            # Set the curr_node as next node
                            node.set_next(curr_node)
                            # Set the node as prev_node's next node
                            prev_node.set_next(node)

                            break
                        prev_node = curr_node
                        curr_node = curr_node.get_next()
                        curr_index += 1

            self._length += 1

    def pop(self, index=0):

        if not self.isEmpty() and index >= 0 and index < self._length:

            flag_remove = False

            # only contains 1 element
            if self._first.get_next() == None:
                self._first = None
                self._last = None
                flag_remove = True

            # first element but contains more elements
            elif index == 0:
                self._first = self._first.get_next()
                flag_remove = True

            # not first element and contains more than 1 element
            else:
                prev_node = self._first
                curr_node = self._first.get_next()
                curr_index = 1

                while curr_node != None:
                    if curr_index == index:
                        prev_node.set_next(curr_node.get_next())
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                    curr_index += 1
            if flag_remove:
                self._length -= 1

    def isEmpty(self):
        if self._length == 0:
            return True
        return False

    def printAll(self):

        curr_node = self._first

        while curr_node != None:
            print(curr_node)
            curr_node = curr_node.get_next()

    def getLength(self):
        return self._length


if __name__ == '__main__':
    lista = LinkedList()
    lista.push("Rodrigo")
    lista.push("Luigi")
    lista.push("Theo")
    lista.push("Leo", 0)
    lista.push("Mãe", 145)
    lista.push("Jean", 2)
    lista.printAll()
    lista.pop()
    lista.pop(lista.getLength()-1)
    lista.printAll()
