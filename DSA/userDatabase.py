

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

database = UserDatabase()

database.insert(akash)
database.insert(viraj)
database.insert(vinay)

database.find('aks')
database.update(User(username='aks',name='zxc',email='mnb@gmail.com'))
database.find('aks')

database.listAll()


