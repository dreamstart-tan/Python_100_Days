class Dict(dict):
    '''
    >>>	import re
    >>>	m = re.search('(?<=abc)def','abcdef')
    >>>	m.group(0)
    'def'
    '''
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

