#模块中应该只有类，如果有其他程序，在运行时也会一起运行

# 当一个模块中的类依赖于另一个模块中的类，可在前一个模块中导入必要的类：
# from car import Car
# from electric_car import ElectricCar

# 使用别名：
# from electric_car import ElectricCar as EC                     # ElectricCar 别名 EC
# my_car = EC()

# import electric_car as ec                                    # 给模块指定别名
# my_car = ec.ElectricCar()                                    # module_name.classname 导入整个模块使用该语法访问具体的类