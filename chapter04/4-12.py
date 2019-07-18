my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

my_foods.append('cannoli') 
friend_foods.append('ice cream') 

for myf in my_foods:
    print(myf)

for frf in friend_foods:
    print(frf)