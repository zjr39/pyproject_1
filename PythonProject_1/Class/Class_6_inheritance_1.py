from Class_3_modify_value import Car                        # 导入Car


class Battery:
    def __init__(self,battery_size =40):           # 默认值是40，可修改 Battery(100)
        self.battery_size = battery_size

    def describe_battert(self)->    '描述电池':
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self)->   '打印电池的续航里程':
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self)->     '更新电池':
        if self.battery_size != 65:
            self.battery_size = 65



# battery = Battery()                          # 找了大半天的问题，问题出在Battery 后面要加().
# battery.describe_battert()                   # 后面也是这个问题，Line21     Bateery()



# 将大型类拆分成多个协同工作的小类，称之为 组合 composition
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()                          # 在初始化属性里，每个实例都包含一个Battery。等于类，也即默认值是40



car_1 = ElectricCar('tesla','model x','2024',)
print('\nElectricCar:')
car_1.car_info()            # 打印车的信息


car_1.battery.describe_battert()        # 打印电池信息
car_1.battery.get_range()               # 打印电池续航里程信息
car_1.battery.upgrade_battery()         # 更新电池
car_1.battery.get_range()               # 打印更新电池后的续航里程信息


