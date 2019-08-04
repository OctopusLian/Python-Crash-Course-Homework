# encoding: utf-8

filename = 'learning_python.txt'

# 第一次打印读取整个文件
print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

# 第二次打印时遍历文件对象
print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

# 第三次打印时将各行存储在一个列表中，再在with代码块外打印它们
print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())