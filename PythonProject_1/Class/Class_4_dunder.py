print('————double underline 双下划线方法————')
#__add__加    __sub__减     __mul__乘     __truediv__除     __iadd__+=      __str__修改字符串


print(f'\n———— __add__ ————')
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def value(self)     -> '打印值':
       return (f'{self.x},{self.y}')

    def __add__(self, other)    -> '两个值相加':
        return Vector2D(self.x + other.x, self.y + other.y)     #这里可以直接用print

v1 = Vector2D(1,1)
v2 = Vector2D(2,2)
v3 = v1+v2
print(v3.value())


print('\n———— __str__ ————')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self)   -> '改变p的返回值':
        return f"姓名：{self.name}，年龄：{self.age}"              #这里必须用return

p1 = Person("张三", 20)
print(p1)
# 当使用 print() 函数打印该类的对象，或者通过 str() 函数将对象转换为字符串时，
# Python 会自动调用这个类中定义的 __str__ 方法，并返回相应的字符串结果


print(f'\n———— 未定义__repr__ ————')
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p2 = Point(1, 2)
print(repr(p2))


print(f'\n———— 定义__repr__ ————')
class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                                        #优先调用__str__
        return f"x：{self.x}，y：{self.y}"


    def __repr__(self)->    '定义__repr__':
        return f"def __repr__ 后返回的字符串"
p3 = Points(1, 2)
print(p3)
print(repr(p3))


#representation 表示
# __repr用于定义对象的 “官方” 字符串表示形式。当在交互式控制台中输入对象名并回车，
# 或者使用repr()函数作用于对象时，就会调用对象所属类的__repr__方法来获取这个表示形式。



#                                    - **目的差异**：
#      - __str__主要用于提供一个对用户友好的、可读性强的对象描述。它的重点在于以一种易于理解的方式展示对象的信息，
# 通常用于像print()这样的场景，面向最终用户或者在输出日志等情况下使用。
#      - __repr__更强调提供一个准确的、能完整表示对象的字符串，它的目标是让开发者可以通过这个字符串来重建对象或者理解对象的内部状态。
# 例如，在调试过程中，__repr__提供的信息可以帮助开发者更好地理解对象的构成。
#                                    - **调用场景差异**：
#      - 当使用print()函数时，通常会优先调用__str__方法。如果没有定义__str__，则会调用__repr__。
#      - 而在交互式控制台中输入对象名或者使用repr()函数时，会调用__repr__方法。