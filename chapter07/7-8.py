# encoding: utf-8

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    finish_sandwich = sandwich_orders.pop()
    print("I made your " + finish_sandwich)
    finished_sandwiches.append(finish_sandwich)

print("\nThe sandwiches have been finished !")
for finish in finished_sandwiches:
    print(finish)