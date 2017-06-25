
# def myfunc():
#     print("myfunc() called.")
#
# myfunc()
# myfunc()

# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
#
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc = deco(myfunc)
#
# myfunc()
# myfunc()
#
# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc()
# myfunc()


# def deco(func):
#     def _deco():
#         print("before myfunc() called.")
#         func()
#         print("  after myfunc() called.")
#         # 不需要返回func，实际上应返回原函数的返回值
#     return _deco
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#     return 'ok'
#
# myfunc()
# myfunc()


# def deco(func):
#     def _deco(a, b):
#         print("before myfunc() called.")
#         ret = func(a, b)
#         print("  after myfunc() called. result: %s" % ret)
#         return ret
#     return _deco
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a + b
#
# myfunc(1, 2)
# myfunc(3, 4)


# def deco(func):
#     def _deco(*args, **kwargs):
#         print("before %s called." % func.__name__)
#         ret = func(*args, **kwargs)
#         print("  after %s called. result: %s" % (func.__name__, ret))
#         return ret
#     return _deco
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a+b
#
# @deco
# def myfunc2(a, b, c):
#     print(" myfunc2(%s,%s,%s) called." % (a, b, c))
#     return a+b+c
#
# myfunc(1, 2)
# myfunc(3, 4)
# myfunc2(1, 2, 3)
# myfunc2(3, 4, 5)

#
# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, arg))
#             func()
#             print("  after %s called [%s]." % (func.__name__, arg))
#         return __deco
#     return _deco
#
# @deco("mymodule")
# def myfunc():
#     print(" myfunc() called.")
#
# @deco("module2")
# def myfunc2():
#     print(" myfunc2() called.")
#
# myfunc()
# myfunc2()



# class locker:
#     def __init__(self):
#         print("locker.__init__() should be not called.")
#
#     @staticmethod
#     def acquire():
#         print("locker.acquire() called.（这是静态方法）")
#
#     @staticmethod
#     def release():
#         print("  locker.release() called.（不需要对象实例）")
#
# def deco(cls):
#     '''cls 必须实现acquire和release静态方法'''
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, cls))
#             cls.acquire()
#             try:
#                 return func()
#             finally:
#                 cls.release()
#         return __deco
#     return _deco
#
# @deco(locker)
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc()
# #myfunc()


from mylocker import *

class example:
    # @lockhelper(mylocker)
    # def myfunc(self):
    #     print(" myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    @lockhelper(lockerex2)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b

if __name__=="__main__":
    a = example()
    #a.myfunc()
    #print(a.myfunc())
    print(a.myfunc2(1, 2))
    #print(a.myfunc2(3, 4))