import pickle 
d = dict(name='Bob',age = 20,score = 88 )
data = pickle.dumps(d)
print(data)

f = open(r'D:\Py100\Python_100_Days\Week4_LXF\res\IO\dump.txt','wb')
pickle.dump(d,f)
f.close()

f = open(r'D:\Py100\Python_100_Days\Week4_LXF\res\IO\dump.txt','rb')
d = pickle.load(f)
print(d)
f.close()










