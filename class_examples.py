# class Foo(object):
#     #sq可以是list
#     def __init__(self,sq):
#         self.sq = sq
#         print('init')
#
#     #obj遍历的时候，调用
#     def __iter__(self):
#         return iter(self.sq)
#
#
# obj = Foo([1,2,3,4,5])
# for i in obj:
#     print(i)


class MyType(type):

    def __init__(self, what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)

        self.__init__(obj)

class Foo(object):

    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo()