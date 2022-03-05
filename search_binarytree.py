class tree_node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def add_child(self, data):
        if data == self.data :
            return
        if data <self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = tree_node(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = tree_node(data)


    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.serch(val)
            return False
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            return False



def build_tree(elements):
        root = tree_node(elements[0])

        for i in range(1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__=='__main__':
    numbers= [5,3,2,1,4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(9))
