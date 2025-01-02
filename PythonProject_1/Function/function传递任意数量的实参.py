def make_pizza(size,*toppings):  
    print(f"\nMakeing a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'mushrooms','green peppers','extra cheese')


#‘*toppings'：创建一个名为toppings的元组，该元组包含函数收到的所有值
