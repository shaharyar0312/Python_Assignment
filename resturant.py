class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Rest name = " + self.restaurant_name + " Cuisine type = "+ self.cuisine_type)
    def  open_restaurant(self):
        print("Restaurant is open")

class  IceCreamStand (Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavour):
        super().__init__( restaurant_name, cuisine_type)
        self.flavour = flavour
    def flavours(self):
        for fl in self.flavour:
            print("flavour: "+fl)

ice = IceCreamStand("Lal Qila", "abcd",["choclate",'strawberry','vanilla'])
ice.flavours()


