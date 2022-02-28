#insert at beggining of linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = node(data)
        new_node.next= self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__=='__main__':
    llist = linkedlist()

    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

    llist.printlist()

    llist.insert(4)
    print('\n')
    llist.printlist()


