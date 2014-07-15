

def deco_args(a,b,num):
    def deco(func):
        def wrapper(*args, **kwargs):
            wrapper.a, wrapper.b = wrapper.b, wrapper.a+wrapper.b
            wrapper.fibseq.append( wrapper.b )
            wrapper.count += 1
            if wrapper.count < num:
                return wrapper(*args)
            else:
                return wrapper.fibseq
        wrapper.count = 0    
        wrapper.a = a
        wrapper.b = b
        wrapper.fibseq = []
        return wrapper
    return deco

# no matter what func want to do, CHANGE it in into a function
# that return fibonacci number sequence
n = 10
@deco_args(a=0,b=1,num=n)
def fib(s):
    print s


print fib('greatest func in the world!')
