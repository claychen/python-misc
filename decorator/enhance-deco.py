# -.- coding=utf-8 -.-
import inspect

def decorator_maker(enhance_decorator):
    def decorator(*args, **kwargs):
        def wrapper(decorated):
            print 'wrapper'
            return enhance_decorator(decorated, *args, **kwargs)
        return wrapper
    return decorator

@decorator_maker
def enhance_decorator(decorated, *args, **kwargs):
    def enhance_wrapper(*argss):
        # Use parameters specified by annotation here
        # Maybe we could use inspect to get details arguments
        # in the decorated funciton
        print 'args' ,args
        print 'kwargs', kwargs
        print argss
        return decorated(*argss)
    return enhance_wrapper

# these argument are for the wrapper, shouldn't be used in 
# decorated funciton
@enhance_decorator(aaa=123,bbb=456)
def decorated(arg1, arg2, arg3= 100): 
    return arg1 + ' ' + arg2 + ' ' + str(arg3)

print decorated('aa','bb' , 200)

