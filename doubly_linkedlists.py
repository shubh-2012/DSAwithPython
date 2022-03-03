#implementation and traversal of doubly linked lists

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class double_ll:
    def __init__(self):
        self.head = None

    def printdlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node

if __name__=="__main__":
    llist = double_ll()
    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third
    second.prev = llist.head
    third.prev = second
    third.next = None

    llist.printdlist()
    print("\n")
    llist.push(4)
    llist.printdlist()



