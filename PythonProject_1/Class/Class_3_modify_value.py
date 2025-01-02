#       * 给属性指定默认值并修改 *

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0                                 #里程数初始值为0    *给属性指定默认值

    def car_info(self):                                 #打印车的信息
        alias = f"{self.make} {self.model} {self.year}"
        print(f"{alias.title()}")

    def modify_odometer(self,miles):                    #修改并打印里程数
        if miles >= self.odometer:                       #防止将里程表回调
            self.odometer = miles
            print(f"The car has {self.odometer} miles on it.")
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self,miles):                 # 让属性的值递增，防止将里程表回调
        self.odometer += miles
        print(f"The car has {self.odometer} miles on it.")


if __name__ == '__main__':         # 只有在本程序中才会运行以下代码
    my_car = Car('audi','A4',2024)        #my_car
    my_car.car_info()
    my_car.modify_odometer(30)
    my_car.increment_odometer(500)
