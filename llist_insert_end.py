
#insert element at end of llist

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")

    def insert_end(self,data):
        temp = self.head
        while(temp.next):
            temp = temp.next
        new_node = node(data)
        temp.next = new_node


if __name__ == "__main__":
    llist = linkedlist()
    llist.head = node(1)
    second = node(2)
    third = node(3)
    llist.head.next = second
    second.next = third

    llist.printlist()

    llist.insert_end(4)

    llist.printlist()


