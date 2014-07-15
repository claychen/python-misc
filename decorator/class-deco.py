
class Deco():
    @staticmethod
    def decorator(arg):
        def maker(func):
            print 'in maker'
            def wrapper():
                print arg
                func()
            return wrapper
        return maker 

@Deco.decorator('hello')
def func():
    print 'in func'

print
func()
