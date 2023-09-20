# singly linked list
# basic operations only, without any checks. eg. check empty before delete etc.
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


class LL:
    head = None

    def insertAtFirst(self, item):
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

    def insertAtEnd(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next

    def insertAtMiddle(self, item, position):
        if position == 1:
            self.insertAtFirst(item)
        else:
            temp = Node(item)
            curr = self.head
            while position > 2:
                curr = curr.next
                position -= 1
            if curr == self.tail:
                self.insertAtEnd(item)
            else:
                temp.next = curr.next
                curr.next = temp

    def removeFirst(self):
        tempHead = self.head
        self.head = self.head.next
        print('item removed at first -> ', tempHead.value)
        del tempHead

    def removeMiddle(self, position):
        originalPosition = position
        if position == 1:
            self.removeFirst()
        else:
            curr = self.head
            while position > 2:
                curr = curr.next
                position -= 1
            if curr.next == self.tail:
                self.removeEnd()
            else:
                temp = curr.next
                curr.next = curr.next.next
                print(
                    f'item removed at position {originalPosition} ->', temp.value)
                del temp

    def removeEnd(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next
        temp = curr.next
        self.tail = curr
        self.tail.next = None
        print('item removed at end-> ', temp.value)
        del temp

    def display(self):
        curr = self.head
        while curr.next:
            print(curr.value, '-> ', end='')
            curr = curr.next
        # last value printed outside loop to avoid -> after last value
        print(curr.value)


l = LL()
l.insertAtFirst(10)
l.insertAtFirst(20)
l.insertAtFirst(30)
l.insertAtFirst('tejas')
l.insertAtMiddle(50, 5)
l.insertAtEnd(60)
l.insertAtMiddle(80, 5)
l.insertAtEnd(70)
l.display()
l.removeFirst()
l.display()
l.removeMiddle(3)
l.display()
l.removeMiddle(6)
l.display()
l.removeEnd()
l.display()
