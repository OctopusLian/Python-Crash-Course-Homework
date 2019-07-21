# encoding: utf-8

# 切记*items这不是指针，是创建一个名为items的空元组，并将收到的所有值都封装到这个元组中
def make_sandwich(*items):
    for item in items:
        print("...adding " + item)

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
