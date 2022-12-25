
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BSTnode:
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


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
#to check whether the tree with given node is BST or not.

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True,None,None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l,min_r,node.key]))
    max_key = max(remove_none([max_l,max_r,node.key]))

    return is_bst_node,min_key,max_key

print(is_bst(node1))

class User:
    def __init__(self,username,name,email): # constructor method.
        self.username = username
        self.name = name
        self.email = email
        print('User Created')

    def introduce_yourself(self,guest_name):
        print("HI {}, I am {} ! , contact me at {} .".format(guest_name,self.name,self.email))

    def __repr__(self):
        return "User(username='{}',name='{}',email='{}')".format(self.username,self.name,self.email)

    def __str__(self):
        return self.__repr__()

jagdesh = User('jag','jagdesh','jag@zyz.com')
biraj = User('bir','biraj','bir@zyz.com')
sonaksh = User('son','sonaksh','son@zyz.com')
aakash = User('aks','akash','aks@zyz.com')
hemanth = User('hem','hemanth','hem@zyz.com')
sidhanth = User('sid','sidhanth','sid@zyz.com')
vishal = User('vis','vishal','vis@zyz.com')

#function to insert new node in BST

def insert(node,key,value):
    if node is None:
        node = BSTnode(key,value)
    elif key < node.key:
        node.left = insert(node.left,key,value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right,key,value)
        node.right.parent = node
    return node

tree = insert(None,jagdesh.username,jagdesh)
insert(tree,biraj.username,biraj)
insert(tree,sonaksh.username,sonaksh)
insert(tree,aakash.username,aakash)
insert(tree,hemanth.username,hemanth)
insert(tree,sidhanth.username,sidhanth)
insert(tree,vishal.username,vishal)

def treeFind(node,key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return treeFind(node.left,key)
    if key > node.key:
        return treeFind(node.right,key)

# ans = treeFind(tree,'son')
# print(ans.value)

#inorder traversal of BST produces sorted list.

def listAll(node):
    if node is None:
        return []
    return (listAll(node.left) + [node.key,node.value] + listAll(node.right))

# result = listAll(tree)
# print(result)

#function to find if a tree is balanced or not.

def isBSTbalanced(node):

    if node is None:
        return True,0

    balanced_l,height_l = isBSTbalanced(node.left)
    balanced_r,height_r = isBSTbalanced(node.right)

    balanced = balanced_r and balanced_l and abs(height_l - height_r) <= 1
    height = 1 + max(height_l,height_r)
    return balanced,height

print(isBSTbalanced(tree))

insert(tree,'tanya',User('tanya','tanya s','tan@xyz.com'))

print(isBSTbalanced(tree))






