from priority_queue import *

a = Item("a", 3)
b = Item("b", 6)
c = Item("c", 1)
d = Item("d", 7)
e = Item("e", 2)
f = Item("f", 9)
g = Item("g", 11)

qp = PriorityQueue()
qp.push(a)
qp.push(b)
qp.push(c)
qp.push(d)
qp.push(e)
qp.push(f)
qp.push(g)

print(qp)

qp.pop()
qp.pop()
print(qp)

qp.push(c)
print(qp)
