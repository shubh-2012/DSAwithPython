


# creating a class user with values name and email.

#operations such as creation, retrieval,updation and deletion.

class User:
    def __init__(self,username,name,email): # constructor method.
        self.username = username
        self.name = name
        self.email = email
        print('User Created')



#what happens here is that python creates an empty object of the type user and stores in the variable user1.
# then invokes the constructor method and argument values are set to the value username,name and email.

#     custom method
    def introduce_yourself(self,guest_name):
        print("HI {}, I am {} ! , contact me at {} .".format(guest_name,self.name,self.email))

user1 = User('shubh','shubham','xyz.com')
user1.introduce_yourself('king')





