
#binary tree traversal using 3 methods.

# 1. inorder traversal
# 2.preorder
# 3. postorder

#inorder -
# (left subtree recursivly inorder,current node,right subtree recursively inorder.

# preorder-
# (current node,left subtree recursivly preorder,right subtree recursively preorder.

def inorder_traversal(node):
    if node is None:
        return []
    return (inorder_traversal(node.left) + [node.val]
            + inorder_traversal(node.right))

def postorder_traversal(node):
    if node is None:
        return []
    return (postorder_traversal(node.left) +  postorder_traversal(node.right)+[node.val])

def preorder_traversal(node):
    if node is None:
        return []
    return ([node.val]
            + preorder_traversal(node.left) +  preorder_traversal(node.right))
def treeHeight(node):
    if node is None:
        return 0
    return 1 + max(treeHeight(node.left),treeHeight(node.right))
