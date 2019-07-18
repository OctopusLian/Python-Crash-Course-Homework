pizza_list = ['red pizze','yellow pizza','green pizza']
friend_pizzas = pizza_list[:]

pizza_list.append('blue pizza')
friend_pizzas.append('black pizza')

print("My pizza:")
print(pizza_list)
print("\n Friend pizza:")
print(friend_pizzas)

for myp in pizza_list:
    print(myp)

for frp in friend_pizzas:
    print(frp)