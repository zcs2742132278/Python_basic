name = '张三'
age = 26
wegiht = 70.0
print('我叫' + name)

# 占位符 %s站位字符串  %i占位整型  %f占位浮点数 %d占位十进制整数 %s是万能的
print(('我叫%s，%i岁，%fkg') % (name, age, wegiht))

info = ('我叫%s，%s岁，%s kg') % (name, age, wegiht)

info2 = ('我叫%s，%s岁，%i kg ,%d') % (name, age, wegiht,wegiht)

print(info)
print(info2)


# f-string  Python 最推荐方式
info3 = f'我叫{name}，{age}岁，{wegiht} kg ,{wegiht}'
print(info3)

print(f'你是{name}，体重正常{wegiht}kg')

# %m.ns %m.nf %m.ni  四舍五入，位数不够，失效
print(('我叫%4s，%1s岁，%2.3s kg') % (name, age, wegiht))
print(('我叫%-4s，%1s岁，%2.3s kg') % (name, age, wegiht))
print(('我叫%.4s，%1s岁，%2.3s kg') % (name, age, wegiht))
print(('我叫%4.1s，%1s岁，%2.3s kg') % (name, age, wegiht))
print(('我叫%1s，%1s岁，%2.3s kg') % (name, age, wegiht))