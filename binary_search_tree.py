"""
Árvores são estruturas de dados hierárquicas. Basicamente, árvores são formadas 
por um conjunto de elementos, os quais chamamos nodos (ou vértices) conectados 
de forma específica por um conjunto de arestas. Um dos nodos, que dizemos estar 
no nível 0, é a raiz da árvore, e está no topo da hierarquia. A raiz está conec-
tada a outros nodos, que estão no nível 1, que por sua vez estão conectados a 
outros nodos, no nível 2, e assim por diante.

Árvores binárias são árvores nas quais cada nodo pode ter no máximo dois filhos,
Uma árvore binária pode ser definida de forma recursiva, de acordo com o raciocínio 
a seguir. A raiz da árvore possui dois filhos, um à direita e outro à esquerda, 
que por sua vez são raizes de duas sub-árvores. Cada uma dessas sub-árvores possui 
uma sub-árvore esquerda e uma sub-árvore direita, seguindo esse mesmo raciocínio.

"""


class Node:

    def __init__(self, label):
        self._label = label
        self._left = None
        self._right = None

    @property
    def label(self):
        return self._label

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setRight(self, label):
        self._right = label

    def setLeft(self, label):
        self._left = label

    def __lt__(self, other):
        return self.label < other.label

    def __le__(self, other):
        return self.label <= other.label

    def __eq__(self, other):
        if other == None:
            return self.label == None
        return self.label == other.label

    def __ne__(self, other):
        if other == None:
            return self.label != None
        return self.label != other.label

    def __gt__(self, other):
        return self.label > other.label

    def __ge__(self, other):
        return self.label >= other.label

    def __str__(self):
        return str(self._label)


class BinarySearchTree:

    def __init__(self):
        self._root = None

    def insert(self, label):

        # create a new Node
        node = Node(label)

        # if tree is empty insert Node as root
        if self.isEmpty():
            self._root = node

        # unempty tree, recusirvely inserts in the right place
        else:
            dad_node = None
            curr_node = self._root

            while True:

                if curr_node != None:

                    dad_node = curr_node

                    # Verify if goes left or right

                    if node < curr_node:
                        curr_node = curr_node.getLeft()
                    else:
                        curr_node = curr_node.getRight()
                else:
                    # if curr is None te code found where to put
                    if node < dad_node:
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    break

    def _how_many_child(self, node):
        if node.getLeft() and node.getRight():
            return 2
        elif node.getLeft() or node.getRight():
            return 1
        else:
            return 0

    def remove(self, label):

        if self.isEmpty():
            return

        node_to_rmv = Node(label)

        dad_node = None
        curr_node = self._root

        while curr_node != None:

            # verifies if node to be removed has been found
            if node_to_rmv == curr_node:
                # how many childs does a node have
                if self._how_many_child(curr_node) == 2:
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.getRight()
                    smallest_node = smaller_node.getLeft()

                    while smallest_node:
                        dad_smaller_node = smaller_node
                        smaller_node = smallest_node
                        smallest_node = smaller_node.getLeft()

                    # Check if the root is the one to be deleted
                    if not dad_node:

                        # verifies if the node that should take the root's place is it's own direct child
                        if self._root.getRight() == smaller_node:
                            smaller_node.setLeft(self.root.getLeft())
                        # changes the place of the root and rerout it's childs
                        else:
                            if dad_smaller_node.getLeft() == smaller_node:
                                dad_smaller_node.setLeft(None)
                            else:
                                dad_smaller_node.setRight(None)

                            smaller_node.setLeft(curr_node.getLeft())
                            smaller_node.setRight(curr_node.getRight())

                        self._root = smaller_node

                    # if it's not the root
                    else:
                        """
                        Verify if curr node is left or right child of dad node
                        to set smaller node as dad_node children
                        """
                        if dad_node.getLeft() == curr_node:
                            dad_node.setLeft(smaller_node)
                        else:
                            dad_node.setRight(smaller_node)

                        """
                        delete dad_smallet_node bond with its old child
                        """

                        if dad_smaller_node.getRight() == smaller_node:
                            dad_smaller_node.setRight(None)
                        else:
                            dad_smaller_node.setLeft(None)

                elif self._how_many_child(curr_node) == 1:

                    # verifies if is the root
                    if dad_node == None:
                        if self._root.getLeft():
                            self._root = curr_node.getLeft()
                        else:
                            self._root = curr_node.getRight()
                    else:
                        # verifies if current_node is left child of dad_node
                        if curr_node < dad_node:
                            # set dad left_node as curr_node left Child
                            dad_node.setLeft(curr_node.getLeft())

                            # if returns it is a Valid node, it ends, if not it changes the child.
                            if not dad_node.getLeft():
                                dad_node.setLeft(curr_node.getRight())

                        # verifies if current_node is right child of dad_node
                        else:
                            # set dad left_node as curr_node right Child
                            dad_node.setRight(curr_node.getRight())

                            # if returns it is a Valid node, it ends, if not it changes the child.
                            if not dad_node.getRight():
                                dad_node.setRight(curr_node.getLeft())

                elif self._how_many_child(curr_node) == 0:

                    # verifies if is the root
                    if dad_node == None:
                        self._root = None

                    else:
                        if dad_node.getRight() == curr_node:
                            dad_node.setRight(None)

                        else:
                            dad_node.setLeft(None)

                break

            dad_node = curr_node

            # Verify if goes left or right

            if node_to_rmv < curr_node:
                curr_node = curr_node.getLeft()
            else:
                curr_node = curr_node.getRight()

    @property
    def root(self):
        return self._root

    def isEmpty(self):
        if not self._root:
            return True
        return False

    def show(self, curr_node):
        if curr_node != None:
            print(curr_node, end=", ")
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())
