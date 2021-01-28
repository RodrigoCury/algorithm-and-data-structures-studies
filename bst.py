from binary_search_tree import BinarySearchTree

if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(1)
    t.insert(6)
    t.insert(4)
    t.insert(7)
    t.insert(10)
    t.insert(9)
    t.insert(14)
    t.insert(13)

    t.show(t.root)
    print(end="\n")

    t.remove(1)

    t.show(t.root)
    print(end="\n")
