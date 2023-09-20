class Queue:
    queue = []
    start = end = -1

    def insert(self):
        item = int(input('enter number\n'))
        self.queue.append(item)
        if self.end == -1:
            self.start = self.end = 0
        else:
            self.end += 1

    def remove(self):
        if self.start > self.end or self.start == -1:
            print('queue empty')
            self.start = self.end = -1
            return
        # because its list, removing item will autoadjust the list. so, we wont delete/remove the element. instead just push the start value
        removedItem = self.queue[self.start]
        print('item removed-> ', removedItem)
        self.start += 1

    def print(self):
        print('\n[ ', end='')
        for i in range(self.start, self.end+1):
            print(self.queue[i], '', end='')
        print(']')


q = Queue()
while True:
    print('-------------------------------')
    choice = int(input('1.insert\n2.remove\n3.Print\n4.Exit\n'))
    match choice:
        case 1:
            q.insert()
        case 2:
            q.remove()
        case 3:
            q.print()
        case 4:
            print('getting out')
            break
        case _:
            print('enter correct choice')
