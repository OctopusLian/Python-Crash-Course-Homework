# encoding: utf-8

m1 = "Zoctopus"
m2 = "nian"
m3 = "Zoctopus"
cars = ['audi', 'bmw', 'subaru', 'toyota']
# 检查两个字符串相等和不等
if m1 == m3:
    print("m1 equal m3")
if m1 != m2:
    print("m1 not equal m2")

# 使用函数lower()的测试
name = 'ADS'
if name.lower() == 'ads':
    print("true")

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于
age = 23
age_1 = 18
if age == 23:
    print("true")
if age > 18:
    print("true")

# 使用关键字and和or的测试
if age > 10 and age_1 < 22:
    print("true")
if age > 25 or age_1 < 25:
    print("true")

# 测试特定的值是否包含在列表中
if 'audi' in cars:
    print("in true")

# 测试特定的值是否未包含在列表中
if 'aaaai' in cars:
    print("not in true")
