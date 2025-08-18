import os
print(os.getcwd())
file = open(r'D:\Py100\Python_100_Days\Day20-30\res\仿橡树.txt','r',encoding = 'utf-8')
print(file.read())
file.close()


file = open(r'D:\Py100\Python_100_Days\Day20-30\res\仿橡树.txt','a',encoding = 'utf-8')
file.write ('\n标题：《真橡树》')
file.write('\n作者:谭生')
file.write('\n时间:1977年3月')
file.close()

file = open(r'D:\Py100\Python_100_Days\Day20-30\res\仿橡树.txt','r',encoding = 'utf-8')
lines = file.readlines()
for line in lines:
    print(line,end='')
file.close()



