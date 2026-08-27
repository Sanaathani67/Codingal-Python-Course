class UserAccount:
    def __init__(self):
        self.username= "sanaa_67"

        #creating a private property
        #2 undersores make it private
        self.__password="1234567890"

    def ShowPassword(self):
        print("Printing from a method inside UserAccount")
        password_length=len(self.__password)
        print("*" *password_length)

#___________________________________________________________

user= UserAccount()
print(user.username)
#print(user.__password)


user.ShowPassword()
