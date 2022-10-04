#tree implementation and traversal

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

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements


def build_tree(elements):
        root = tree_node(elements[0])

        for i in range(1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__=='__main__':
    numbers= [90,4,5,72,12,3,5,5]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inorder_traversal())
