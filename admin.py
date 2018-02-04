class User():
    def __init__(self,f_name,l_name, age ):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def describe_user(self):
        print ("Mr." + self.f_name + self.l_name + "having an age of " + self.age)
    def greet_user(self):
        print("welcome "+ self.f_name + self.l_name)

class Admin(User):
    def __init__(self,f_name, l_name,age,privileges):
        super().__init__(f_name,l_name,age)
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(self.f_name, self.l_name + privilege)

admin = Admin("Richard", "Handricks", 28, [ " can add post", " can delete post", " can ban user"])
admin.show_privileges()