class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class binaryTree:
    root = None

    def __init__(self):
        print('build tree'.center(30, '-'))
        print('enter root value')
        self.root = self.insertRecursive(self.root)
        print('tree build complete'.center(30, '-'))

    # recursively insert to build the tree
    def insertRecursive(self, root):
        item = int(input())
        if item == 0:
            return root
        node = Node(item)
        print('enter left of ', item)
        node.left = self.insertRecursive(node.left)
        print('enter right of ', item)
        node.right = self.insertRecursive(node.right)
        return node

    # driver function for search
    def searchItem(self):
        print('search element in BST'.center(30, '-'))
        searchEl = int(input('enter element to search'.center(30, '-')))
        isPresent = self.search(self.root, searchEl)
        if isPresent:
            print('Element present')
        else:
            print('Element not present')
        print('item search complete'.center(30, '-'))

    # search if element is present
    def search(self, root, el):
        if not root:
            return False
        if root.item == el:
            return True
        if el < root.item:
            return self.search(root.left, el)
        elif el > root.item:
            return self.search(root.right, el)

    # driver for insert new
    def insertItem(self):
        print('Inserting new item in BST'.center(30, '-'))
        newEl = int(input("enter new element to insert"))
        self.root = self.insertNewItem(self.root, newEl)
        print('insert new item complete'.center(30, '-'))

    # insert new element
    def insertNewItem(self, root, item):
        if not root:
            return Node(item)
        elif root.item == item:
            print('element already present')
            return root
        elif item > root.item:
            root.right = self.insertNewItem(root.right, item)
        elif item < root.item:
            root.left = self.insertNewItem(root.left, item)
        return root

    # driver for remove item
    def removeItem(self):
        itemToRemove = int(input(('enter item to remove')))
        # find the item in tree
        isPresent = self.search(self.root, itemToRemove)
        if not isPresent:
            print('Element not present')
        else:
            self.root = self.removeItemFromBST(self.root, itemToRemove)
        # find the left most leaf of the immediate right subtree of found root

    # remove item
    def removeItemFromBST(self, root, el):
        if not root:
            return None
        elif el > root.item:
            root.right = self.removeItemFromBST(root.right, el)
        elif el < root.item:
            root.left = self.removeItemFromBST(root.left, el)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                tempRoot = self.findMin(root.right)
                root.item = tempRoot.item
                root.right = self.removeItemFromBST(root.right, tempRoot.item)
        return root
    # find minimum of any subtree

    def findMin(self, root):
        tempRoot = root
        while tempRoot.left:
            tempRoot = tempRoot.left
        print('smallest is ->', tempRoot.item)
        return tempRoot

    # driver for printBT
    def printBST(self):
        print('displaying the tree'.center(30, '-'))
        print('root item ->', end='')
        self.printBT(self.root)
        print('display tree complete'.center(30, '-'))
    # print the tree

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
while True:
    print('\n1.Insert\n2.Remove\n3.Print\n4.is item present?\n5.Exit')
    choice = int(input())
    match choice:
        case 1:
            bt.insertItem()
        case 2:
            bt.removeItem()
        case 3:
            bt.printBST()
        case 4:
            bt.searchItem()
        case 5: break
