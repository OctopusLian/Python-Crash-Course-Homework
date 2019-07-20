# encoding: utf-8

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

# 打印该字典中每条河流的名字
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

#打印该字典中包含的每个国家的名字
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())