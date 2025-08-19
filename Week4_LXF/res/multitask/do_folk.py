'''
fork windows 系统不支持，只能在MAC上使用
'''
import os 
print('Process (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' %(os.getpid(),pid))
























