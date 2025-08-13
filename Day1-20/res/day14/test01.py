"""
输入m和n，计算组合数C(m,n)的值
Version: 1.0
Author:谭小品
"""
from math import factorial
m = int(input('m = '))
n = int(input('n = '))

print(factorial(m) // factorial(n) // factorial(m-n)) 






























