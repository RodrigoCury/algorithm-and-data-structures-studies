"""
    Uma pilha é um tipo de dado abstrato muito utilizado em computação. 
Seu nome é devido a analogia do comportamento dessa estrutura com pilhas de objetos no mundo real. 
Considere por exemplo uma pilha de livros. 
Um novo livro deve ser colocado no topo, assim como o primeiro livro a ser retirado deve sair do topo também.

    Uma pilha (=*stack*) é uma lista dinâmica em que todas as operações (inserções, remoções e consultas)
são feitas em uma mesma extremidade chamada de topo. 
Portanto, em uma estrutura do tipo pilha, o último elemento que inserido é o primeiro a ser removido ou consultado. 
Essa estrutura também é conhe(conhecido como LIFO do inglês last-in first-out).
"""


class Stack:  # Pilha

    def __init__(self):
        self.stack = []

    def insert(self, el):
        self.stack.append(el)

    def delete(self):
        if not self.isEmpty():
            self.stack.pop(-1)

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return ("Empty Stack")

    def is_empty(self):
        if(len(self.stack) == 0):
            return True
        return False

    def lenght(self):
        return len(self.stack)

    def __str__(self):
        string = ""
        for e in self.stack:
            string = string + e + ", "
        return string


class OptmizedStack():

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def insert(self, el):
        self.stack.append(el)
        self.len_stack += 1

    def delete(self):
        if not self.isEmpty():
            self.stack.pop(-1)
            self.len_stack -= 1

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def is_empty(self):
        if(self.len_stack != None):
            return True
        return False

    def lenght(self):
        return self.len_stack

    def __str__(self):
        string = ""
        for e in self.stack:
            string = string + e + ", "
        return string
