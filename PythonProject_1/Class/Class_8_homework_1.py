class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):            #餐馆名字，菜系类型
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0                                   # 就餐人数

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now opening.")

    def set_number_served(self,headcount):                          # 有'headcount'人在这家餐馆就餐
        if headcount >= self.number_served:
            self.number_served = headcount
            print(f"There are {self.number_served} people who have dined at this restaurant.")
        else:
            print(f"Warning!"
                  f"The headcount is not right!")

    def increment_number_served(self,headcount):
        self.number_served += headcount
        print(f"这家餐馆每天可能接待{self.number_served}人")

restaurant = Restaurant('功德林','淮扬菜')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(30)
restaurant.increment_number_served(70)



class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def describe_flavors(self)->  '描述口味':
        for flavor in self.flavors:                         # 必须是self.flavors
            print('-'+flavor)

icecream = IceCreamStand("哈迪达斯","冰淇淋",['香草','草莓','牛奶巧克力','榛子巧克力'])
icecream.describe_flavors()