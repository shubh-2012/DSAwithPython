
#insert node after given node in linkedlist

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_node(self, data , prev):
        new_node = node(data)
        new_node.next = prev.next
        prev.next = new_node

    def print_linkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")

llist = linkedlist()

llist.head = node(1)
second = node(2)
third = node(3)

llist.head.next = second
second.next = third

llist.print_linkedlist()

llist.insert_node(5, second)

llist.print_linkedlist()
