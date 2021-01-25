"""
Em ciência da computação, uma Fila Duplamente Terminada (frequentemente abreviada como DEQUE,
do inglês Double Ended Queue) é um tipo de dado abstrato que generaliza uma fila, para a qual
os elementos podem ser adicionados ou removidos da frente (cabeça) ou de trás (cauda).[1] 
Também é chamada de lista encadeada cabeça-cauda, apesar de propriamente isto se referir a uma
implementação de estrutura de dados específica. 
"""
from collections import deque


class Deque():
    def __init__(self):
        self.deque = []
        self.len = 0

    def is_empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, el):
        self.deque.insert(0, el)
        self.len += 1

    def push_back(self, el):
        self.deque.append(el)
        self.len += 1

    def pop_front(self):
        if not self.is_empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.is_empty():
            self.deque.pop(self.len - 1)
            self.len -= 1

    def __str__(self) -> str:
        string = ''
        if not self.is_empty():
            for i in self.deque:
                string += str(i) + "\n"
            return string
        return "[]"


if __name__ == '__main__':
    d = Deque()

    d.push_front(1)
    d.push_front(2)
    d.push_back(0)
    d.push_back(-1)
    d.push_back(-2)
    print(d)
    d.pop_front()
    d.pop_back()
    print(d)
    print(d)

    q = deque()
    q.append(1)
    q.appendleft(2)
    q.append(3)
    q.appendleft(4)
    q.popleft()
    q.pop()
    for i in q:
        print(i, end="")
