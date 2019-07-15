names = ['David','Susan','Kitty']
print(names)
names.remove('Susan')
print(names)
names.append('Herry')
print(names)

names.insert(0,'Zoctopus')
names.insert(2,'Lianlian')
names.append('Niannian')
print(names)

names_pop1 = names.pop()
print(names_pop1)
names_pop2 = names.pop()
print(names_pop2)
names_pop3 = names.pop()
print(names_pop3)
names_pop4 = names.pop()
print(names_pop4)

print(names)

del names[1]
print(names)
del names[0]
print(names)
