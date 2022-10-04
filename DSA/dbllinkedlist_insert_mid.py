#implementation and traversal of doubly linked lists
#add node in mid

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

    def insert_at(self,data,x):
        temp = self.head
        while(temp != x):
            temp = temp.next

        new_node = node(data)
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

if __name__=="__main__":
    llist = double_ll()
    first = node(1)
    llist.head = first
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third
    second.prev = llist.head
    third.prev = second
    third.next = None

    llist.printdlist()
    print("\n")
    llist.insert_at(4,second)
    llist.printdlist()



