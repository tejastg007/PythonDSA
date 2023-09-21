# doublu linked list with only insertfirst, insertend, removefirst,removeend functionality. no checks for empty list before removing elements 
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None
        self.prev = None


class DLL:
    def __init__(self, item):
        print('head initialized with-> ', item, '\n')
        self.head = Node(item)
        self.tail = self.head

    def insertFirst(self, item):
        print('insert at first item-> ', item)
        tempNode = Node(item)
        tempNode.next = self.head
        self.head.prev = tempNode
        self.head = tempNode

    def insertEnd(self, item):
        print('insert at end item-> ', item)
        tempNode = Node(item)
        self.tail.next = tempNode
        tempNode.prev = self.tail
        self.tail = tempNode

    def removeFirst(self):
        tempNode = self.head
        print('item removed at first-> ', tempNode.value)
        self.head = self.head.next
        self.head.prev = None
        del tempNode

    def removeEnd(self):
        tempNode = self.tail
        print('item removed at end-> ', tempNode.value)
        self.tail = self.tail.prev
        self.tail.next = None
        del tempNode

    def display(self):
        curr = self.head
        while curr.next:
            print(curr.value, ' ', end='')
            curr = curr.next
        if curr:
            print(curr.value, '\n')
        else:
            print('list empty')


d = DLL(12)
d.insertFirst(10)
d.display()
d.insertFirst(30)
d.display()
d.insertEnd(40)
d.display()
d.removeFirst()
d.display()
d.removeFirst()
d.display()
d.removeEnd()
d.display()
print('Head value-> ', d.head.value)
print('tail Value-> ', d.tail.value)
