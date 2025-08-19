try:
    print('try...')
    m = int(input('请输入除数:'))
    r = 10 / m
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')








