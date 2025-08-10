"""
 功能简介：
 Version: 1.0
 Author : 谭小品
 """
set1 = {1,3,5,7}
set2 = {2,4,6}
set1 |=set2

print(set1)
set3 = {3,6,9}
set1 &= set3
print(set1)
set2 -= set1
print(set2)







