'''从本质上讲，装饰器是一个函数，这个函数接受另一个函数（或类）作为参数，并且返回一个新的函数（或类）'''

'函数作为一等对象可以作为参数传递到函数中'
def square(x):
    '''x的平方'''
    return x*x

def print_running(f,x):
    '''此函数接受 一个函数f，和一个数字x 作为参数'''
    print(f'{f.__name__} is runing.')           # 打印函数的名字
    return f(x)

result = print_running(square,2)
print(result)


'''装饰器实例'''
def decorator(func):
    def wrapper(*args,**kwargs):    # 无论什么参数，wapper都可以吃下去
        print(f'{func.__name__} is runing.')
        result = func(*args,**kwargs)           # wrapper用来运行本来func的功能
        return result
    return wrapper


'''一个测量函数运行时间的装饰器'''
import time

def decorator_time(func):
    def wrapper(*args,**kwargs):    # 无论什么参数，wapper都可以吃下去
        start_time = time.time()    # 获取代码块开始执行的时间戳
        result = func(*args,**kwargs)
        end_time = time.time()      # 获取代码块结束执行的时间戳
        print(f"{func.__name__} execution time: {end_time-start_time} seconds.")    # 得到代码的执行时间
        return result
    return wrapper

# time.time()是time模块中的一个函数，它返回从 1970 年 1 月 1 日 00:00:00 UTC 到当前时刻的以秒为单位的时间戳（time stamp）。
# 时间戳是一个浮点数，它表示的是一个特定的时刻在时间轴上的位置，这对于记录事件发生的时间、计算时间间隔等操作非常有用。

'''如何使用装饰器'''
square = decorator_time(square)    # 因为装饰后的函数是为了代替原来的函数，所有可以直接用函数square
square(10)                         # square是被decorator_time(square)装饰后的函数

'''实际上，python 有更便捷的方式使用装饰器 '''
@decorator_time
def square(x):
    '''x的平方'''
    return x*x

square(10)


'''测量函数运行的时间是否超过了阈值'''
def timer(threshold):
    def decorator_time(func):
        def wrapper(*args,**kwargs):    # 无论什么参数，wapper都可以吃下去
            start_time = time.time()    # 获取代码块开始执行的时间戳
            result = func(*args,**kwargs)
            end_time = time.time()      # 获取代码块结束执行的时间戳
            if end_time-start_time > threshold:
                print(f"{func.__name__} took longer than {end_time-start_time} seconds.")    # 得到代码的执行时间
            return result
        return wrapper
    return decorator_time


'''如果使用它'''
@timer(0.2)
def sleep_04():
    time.sleep(0.4)

sleep_04()

# 这个定义等价于
# sleep_04() = timer(0.2)(sleep_04)
# timer(0.2) 是装饰器，再将(sleep_04) 传给装饰器


print(sleep_04.__name__) # 因为装饰器后返回的是在装饰器里面定义的wrapper,所以返回wrapper

# 如何让wapper继承原函数的属性
# import functools
# def timer(threshold):
#     def decorator_time(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):    # 无论什么参数，wapper都可以吃下去
#             start_time = time.time()    # 获取代码块开始执行的时间戳
#             result = func(*args,**kwargs)
#             end_time = time.time()      # 获取代码块结束执行的时间戳
#             if end_time-start_time > threshold:
#                 print(f"{func.__name__} took longer than {end_time-start_time} seconds.")    # 得到代码的执行时间
#             return result
#         return wrapper
#     return decorator_time
#
# print(sleep_04.__name__)


"""
使用装饰器的三个原因
    1.使用装饰器可以提升代码复用，避免重复冗余代码。如果我有多个函数需要测量运行时间，我可以直接将装饰器应用在这些函数上，
        而不是给多个函数加上一样的代码。这样的代码既冗余也不方便后面维护。
    2.使用装饰器可以保证函数的逻辑清晰。如果一个本身功能就很复杂的函数，我还要通过修改内部代码来测量运行时间，这样会模糊函数自身的主逻辑。
        同时，软件开发的一个原则就是单一职责，也就是说，一个函数只应该承担一项责任。
    3.通过装饰器，我们可以扩展别人的函数。比如我们正在使用一个第三方库的函数，但我要添加额外的行为，比如测量运行时间，
        那我就可以用装饰器去包装，而不是跑到库里面去修改。
"""

