"""
 功能简介：尝试列表元素的不同删除方法
 Version: 1.0
 Author : 谭小品
 """
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)
