class User():
    def __init__(self,f_name,l_name, age ):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def describe_user(self):
        print ("Mr." + self.f_name + self.l_name + "having an age of " + self.age)
    def greet_user(self):
        print("welcome "+ self.f_name + self.l_name)
class Privilege():
    def __init__(self, privilege = [ " can add post", " can delete post", " can ban user"]):
        self.privilege = privilege
    def show_privilege(self):
        for privilege in self.privilege:
            print("Admin " + privilege)

class Admin(User):
    def __init__(self,f_name, l_name,age):
        super().__init__(f_name,l_name,age)
        self.privilege = Privilege()

admin = Admin('shaharyar', 'azam', 22)
admin.privilege.show_privilege()