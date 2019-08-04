# encoding: utf-8  

class Restaurant():
    # 创建一个饭馆的类

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

# IceCreamStand继承Restaurant类
class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = [] # 存储一个由各种口味的冰淇淋组成的列表

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()