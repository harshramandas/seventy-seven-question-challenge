class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
def printAll(head):
    if not head:
        print("|")
    else:
        print(str(head.data)+" -> ", end = "")
        printAll(head.next)
def printReverse(head):
    if not head:
        print("|")
    else:
        printReverse(head.next)
        print(str(head.data)+" -> ", end = "")

def insertBeg():
    global head
    if head:
        temp = head
        head = Node(int(input("Enter data: ")))
        head.next = temp
    else:
        head = Node(int(input("Enter data: ")))
    printAll(head)

def insertEnd():
    global head
    if head:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(int(input("Enter data: ")))
    else:
        head = Node(int(input("Enter data: ")))
    printAll(head)

def insertAfter():
    global head
    n = int(input("Enter no. after which you want to enter: "))
    temp = head
    flag = 0
    while temp:
        if temp.data == n:
            node = Node(int(input("Enter data: ")))
            node.next = temp.next
            temp.next = node
            flag = 1
        break
    if flag == 0:
        print("No such element found")
    printAll(head)

def insertBefore():
    global head
    n = int(input("Enter no. before which you want to enter: "))
    temp = head
    flag = 0
    if temp.data != n:
        while temp.next:
            if temp.next.data == n:
                node = Node(int(input("Enter data: ")))
                node.next = temp.next.next
                temp.next = node
                flag = 1
            break
    else:
        node = Node(int(input("Enter data: ")))
        node.next = head.next
        head = node
        flag = 1
    if flag == 0:
        print("No such element found")
    printAll(head)

def deleteBeg():
    global head
    if head:
        head = head.next
    else:
        print("Empty List!")
    printAll(head)

def deleteEnd():
    global head
    if head:
        temp = head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None
    elif head and not head.next:
        head = None
    else:
        print("Empty List!")
    printAll(head)

def deleteSpecific():
    global head
    n = int(input("Enter no. which you want to delete: "))
    temp = head
    flag = 0
    if head and head.data == n:
        head = head.next
        flag = 1
    elif head and head.next and head.next.data == n:
        head.next = head.next.next
    elif head and head.next:
        while temp.next.next:
            if temp.next.data == n:
                if temp.next.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
                flag = 1
                break
            temp = temp.next
    if flag == 0:
        print("No such element found")
    printAll(head)

while True:
    print("\nEnter :- ")
    print("1 to Insert element at beginning.")
    print("2 to Insert element at end.")
    print("3 to Insert element after a specific element.")
    print("4 to Insert element before a specific element.")
    print("5 to Delete element at beginning.")
    print("6 to Delete element at end.")
    print("7 to Delete a specific element.")
    print("8 to Print all elements")
    print("9 to Print all in reverseOrder")
    print("0 to exit!")
    c = int(input("Enter choice: "))
    if c == 1:
        insertBeg()
    elif c == 2:
        insertEnd()
    elif c == 3:
        insertAfter()
    elif c == 4:
        insertBefore()
    elif c == 5:
        deleteBeg()
    elif c == 6:
        deleteEnd()
    elif c == 7:
        deleteSpecific()
    elif c == 8:
        printAll(head)
    elif c == 9:
        printReverse(head)
    else:
        print("Wrong Choice Enter Again!")
