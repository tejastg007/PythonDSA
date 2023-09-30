class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class binaryTree:
    root = None

    def __init__(self):
        print('enter value for root')
        self.root = self.insert(self.root)
        print('root value - ', end='')
        self.printBT(self.root)

    def insert(self, root):
        item = int(input())
        if item == -1:
            return root

        node = Node(item)
        print('enter left of ', item)
        node.left = self.insert(node.left)
        print('enter right of ', item)
        node.right = self.insert(node.right)
        return node

    def display(self):
        self.printBT(self.root)

    def printBT(self, root):
        if root == None:
            print('None')
            return
        print(root.item)
        print('left of', root.item, '->', end='')
        self.printBT(root.left)
        print('right of', root.item, '->', end='')
        self.printBT(root.right)


bt = binaryTree()
