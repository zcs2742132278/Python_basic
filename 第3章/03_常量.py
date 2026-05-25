import sys
from operator import concat

age = 10
print(age)

age = 111
print(age)
age = '!@#!'
print(age)

# 数据类型
print(type(age))

# ** 平方
print(300_000, 30_00, 300_000_000, 3 ** 2)

# 取消整数位数限制
sys.set_int_max_str_digits(0)

a = 3.4e2  # 科学技术法 e2 = 是的二次方  e3=10的三次方
b = 3e7  # 科学技术法 e2 = 是的二次方  e3=10的三次方

print(a, b)

print(concat('1213', '2113'), len('wdafsa'))

#
print('张三'

      '打'
      '三角洲')
