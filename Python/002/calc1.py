#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # 使用input()函数读取键盘输入
str1 = input("请输入第一个操作数： ")
str2 = input("接下来是第二个操作数： ")

# 使用int()函数，这是把键盘读取的输入字符转换为整数的函数
x = int(str1)
y = int(str2)

# 输出计算结果
print(x, "+", y, " = ", x+y)
print(x, "-", y, " = ", x-y)
print(x, "*", y, " = ", x*y)
print(x, "**", y, " = ", x**y)
print(x, "/", y, " = ", x/y)
print(x, "//", y, " = ", x//y)