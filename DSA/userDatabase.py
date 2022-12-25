

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

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i=0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)


    def update(self,user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        print('user {} updated'.format(user.username))

    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user


    def listAll(self):
        print(self.users)
        return self.users

akash = User('aks','akash','aks@zyz.com')
viraj = User('vir','viraj','vir@zyz.com')
vinay = User('vin','vinay','vin@zyz.com')
kabir = User('singh','kabir','singh@zyz.com')

# users = [akash,viraj,vinay,kabir]

# print(akash)
# print(users)

# database = UserDatabase()
#
# database.insert(akash)
# database.insert(viraj)
# database.insert(vinay)
#
# database.find('aks')
# database.update(User(username='aks',name='zxc',email='mnb@gmail.com'))
# database.find('aks')
#
# database.listAll()


jagdesh = User('jag','jagdesh','jag@zyz.com')
biraj = User('bir','biraj','bir@zyz.com')
sonaksh = User('son','sonaksh','son@zyz.com')
aakash = User('aks','akash','aks@zyz.com')
hemanth = User('hem','hemanth','hem@zyz.com')
sidhanth = User('sid','sidhanth','sid@zyz.com')
vishal = User('vis','vishal','vis@zyz.com')

#storing key value pair in BST

class BSTnode:
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# tree = BSTnode(akash.username,akash)
#
# tree.left = BSTnode(viraj.username,viraj)
# tree.left.parent = tree
# tree.right = BSTnode(vinay.username,vinay)
# tree.right.parent = tree
# print(tree.value,tree.key)

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

def update(node,key,value):
    target = treeFind(node,key)
    if target is not None:
        target.value = value

update(tree,'vis',User('vis','Vishal S','vis@gmail.com'))
ans = treeFind(tree,'vis')
print(ans.key,ans.value)


