
from datetime import datetime

with open(r'D:\Py100\Python_100_Days\Week4_LXF\res\IO\test01.txt','w') as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y-%m-%d'))
with open(r'D:\Py100\Python_100_Days\Week4_LXF\res\IO\test01.txt','r') as f:
    s = f.read()
    print('Open for read...')
    print(s)

with open(r'D:\Py100\Python_100_Days\Week4_LXF\res\IO\test01.txt','rb') as f:
    s = f.read()
    print('Open as binary for read...')
    print(s)



