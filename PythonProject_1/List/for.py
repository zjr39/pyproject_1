squares = []
for value in range(0,11,2):         #range(start,stop,step)
    square=value**2
    squares.append(square)
print(f"\nsquares:")
print(squares)

squares_1 = [value**2 for value in range(0,11,2)]       #列表推导式
print(f"\n列表推导式:")
print(squares_1)

list_1 = [value for value in range(3,31) if value % 3 ==0]      #列表推导式带if条件
print(f"\n创建一个列表，其中包含3-30内能被3整除的数：")
print(list_1)


#切片slice        [start,stop,step] ———— 注意是方括号
numbers = list(range(0,11))
print(f"\n切片:")
print(numbers[5:8])
print(numbers[-3:])
print(numbers[:6])
print(numbers[::2])
#for number in numbers[-8,-1]:        遍历切片


