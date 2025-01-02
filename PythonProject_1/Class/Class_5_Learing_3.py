# 面向对象的三大特性 封装 继承 多态
# 封装：把共性（属性，函数）搞在一起变个类
# 继承：子类继承父类的属性，函数
# 多态：子类继承父类的同名函数，可在子类修改以拥有不同的效果

# 类的属性 VS 对象的属性
# 类的属性属于类，并且所有该类的对象都共享这个属性
# 对象的属性属于对象     self.xxxx

class Animal:

    bu_ru_dong_wu = True                                        # 类的属性，不用初始化，所有对象共享

    def __init__(self,name):
        self.name = name

    def __eat(self):                                            # __方法 不会继承到子类
        print('此函数不会被继承')                                  # __属性 不会继承到子类 (self.__name = name)

    def sound(self):
        pass                                                    # 函数具体定义在子类



class Dog(Animal):                                              # 子类
    def __init__(self,name):
        super().__init__(name)                                  # 把父类的初始化属性 传参 到子类

    def sound(self):
        print('汪汪汪')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print('喵喵喵喵')

    @classmethod                                                # 在对象的函数前面加上@classmethod，就变成了类的函数
    def piss(self)->        '尿尿':
        print('尿尿')


def makesound(animal)->     '叫声':                              # animal 就是Animal的对象
    animal.sound()

dog = Dog("旺财")
cat = Cat('咪咪')
print(dog.name)
makesound(dog)
makesound(cat)
print(Animal.bu_ru_dong_wu)



