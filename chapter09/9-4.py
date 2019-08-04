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
    # 设置就餐人数
    def set_number_served(self,number_served):
        self.number_served = number_served
    # 将就餐人数递增
    def increment_number_served(self, additional_served):
        self.number_served += additional_served 

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.set_number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))   

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))