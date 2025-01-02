#标准库 Standard Library
from random import randint                      # randint()将两个整数作为参数，并随机返回一个位于这两个整数之间（含）的整数

class Die:
    def __init__(self,sides)->      '骰子的面数':
        self.sides = sides

    def roll_die(self)->        '打印位于1和骰子面数之间的随机数':
        print(randint(1,self.sides))

die = Die(20)
die.roll_die()                  # roll骰子



from random import choice                      # chice()将一个列表或元组作为参数，并随机返回其中的一个元素

lottery = [8,65,15,5,78,35,2,6,45,68,'d','j','k','g','y']           # 彩票
lottery_1 = choice(lottery)
lottery_2 = choice(lottery)
lottery_3 = choice(lottery)
lottery_4 = choice(lottery)
lottery_ticket = f"{lottery_1},{lottery_2},{lottery_3},{lottery_4}"
print(f"今天的彩票号码有：{lottery_ticket}")



import random

# 创建包含10个数字和5个字母的列表，这里简单示例，数字用0-9表示，字母用a-e表示
origin_list = list(range(10)) + ['a', 'b', 'c', 'd', 'e']

# 定义自己的彩票号码列表（示例，这里随意选取4个元素）
my_ticket = random.sample(origin_list, 4)

# 用于记录循环次数
count = 0
while True:
    # 每次随机选择4个元素作为抽取的号码
    picked_numbers = random.sample(origin_list, 4)
    count += 1
    if picked_numbers == my_ticket:
        print(f"经过了{count}次循环，终于中大奖了！")
        break


