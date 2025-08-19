import logging
logging.basicConfig(filename=r'D:\Py100\Python_100_Days\Week4_LXF\res\test.log',level = logging.DEBUG)
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')





