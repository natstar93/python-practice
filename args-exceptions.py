import sys

try: 
    total = sum(int(arg) for arg in sys.argv[1:]) # sys.argv[1:] is everything after the [0] args (script name)
    print('sum = {0}'.format(total))
except:
    print('please supply integer arguments')