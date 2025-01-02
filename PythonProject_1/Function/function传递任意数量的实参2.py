def make_sandwich(*toppings):  
    print('Making a sandwich with following toppings:')
    for topping in toppings:  
        print("-" + topping)         

sandwich_toppings=input('请输入想要添加的食材,不同食材之间用逗号隔开:').split(",")
make_sandwich(*[i.strip() for i in sandwich_toppings])   #列表推导式

#如果没用空格可使用：make_sandwich(*sandwich_toppings)



#首先 split(",") 得到 [" 火腿", " 生菜", " 番茄"],
#经过 [i.strip() for i in sandwich_ingredients]处理后
#变为 ["火腿", "生菜", "番茄"]，
#再通过 * 操作符解包传递给 make_sandwich 函数。


#split是 Python 字符串的一个方法，用于将一个字符串按照指定的分隔符进行分割，
#并返回一个包含分割后子字符串的列表。
#语法：str.split(separator, maxsplit)。
#其中separator是分隔符，默认是空格；maxsplit是最大分割次数，
#可选参数，默认是将字符串全部分割。
#分隔符优先用英文逗号，如果要用中文逗号，split("，")
