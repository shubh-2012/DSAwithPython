#class to represent binary node.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# if __name__ == '__main__':
#
#     root = Node(1)
#
#     root.left = Node(2)
#     root.right = Node(3)
#
#     root.left.left = Node(4)

# it's inconvinient to add nodes manually , so we can use tuple to store values.
# values in tuple are stored with structure (left_subtree,key,right_subtree),
# where left_subtree and right_subtree are themselves tuple.

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):  #function to convert tuple to tree.

    if isinstance(data,tuple) and len(data) == 3:
        node = Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    return node

node1 = parse_tuple(tree_tuple)
#
# print(node1.val)
# print(node1.left.val)
# print(node1.right.val)

#try converting tree to tuple.

def inorder_traversal(node):
    if node is None:
        return []
    return (inorder_traversal(node.left) + [node.val]
            + inorder_traversal(node.right))

def postorder_traversal(node):
    if node is None:
        return []
    return (postorder_traversal(node.left) +  postorder_traversal(node.right) + [node.val])

def preorder_traversal(node):
    if node is None:
        return []
    return ([node.val]
            + preorder_traversal(node.left) + preorder_traversal(node.right))
def treeHeight(node):
    if node is None:
        return 0
    return 1 + max(treeHeight(node.left),treeHeight(node.right))

result = inorder_traversal(node1)
result1 = preorder_traversal(node1)
result2 = postorder_traversal(node1)

print(result)
print(result1)
print(result2)

print(treeHeight(node1))





