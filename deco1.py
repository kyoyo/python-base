def a(func):
    def _deco():
        print("this is a")
        func()

    return _deco

def b(func):
    def _deco():
        print("this is b")
        func()

    return _deco

def c(func):
    def _deco():
        print("this is c")
        func()

    return _deco


@a
@b
@c
def myfunc():
    print("hello myfunc")

#myfunc()