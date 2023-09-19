stack = []
top = 0


def insert():
    item = int(input('enter item\n'))
    global top
    stack.append(item)
    top += 1


def pop():
    global top
    if top == 0:
        print('list is already empty')
        return
    poppedItem = stack.pop()
    top -= 1
    print('poppedItem-> ', poppedItem)


def display():
    global stack
    print(stack)


while True:
    choice = int(input('\n1.insert\n2.pop\n3.Print\n4.Exit\n'))
    match choice:
        case 1:
            insert()
        case 2:
            pop()
        case 3:
            display()
        case 4:
            print('getting out')
            break
        case _:
            print('enter correct choice')
