favorite = ['看书','游泳','拳击','玩游戏']

#修改列表元素
favorite[0]='刷抖音'
print(f'修改后的列表元素：\n{favorite}')


#添加列表元素
favorite.append('码字')       #在列表末尾添加元素
print(f'\n.append()：\n{favorite}')

favorite.insert(0,'溜冰')     #在列表中添加元素
print(f'\n.insert():\n{favorite}')


#删除列表元素
del favorite[-1]                    #删除后无法访问被删除的值
print(f'\ndel:\n{favorite}')

popped_favorite=favorite.pop()      #会改变原列表，其实是值的转移
print(f'\n.pop():\n{favorite}')     #默认删除最后一个元素
print(popped_favorite)

popped_favorite=favorite.pop(0)     #.pop()也可删除列表中任意位置的元素
print(f'\n.pop(0):\n{favorite}')    #如果在删除元素后不再使用它，用del；如果要在删除元素后继续使用它，用pop()
print(popped_favorite)

favorite.remove('刷抖音')            #删除具体元素
print(f'\n.remove():\n{favorite}')

removed_favorite = '拳击'            #.remove()也可访问被删除的值，把被删除的值赋给另一个变量
favorite.remove(removed_favorite)
print(f'\nremoved:\n{favorite}')
print(removed_favorite)

#.remove()只能删除第一个值。如果要删除的值在列表中多次出现，就需要用while
pets = ['dog','cat','pig','cat','fox','cat']
while 'cat' in pets:
    pets.remove('cat')
print(f'\nwhile remove():\n{pets}')
#使用'while True' 会一直删除cat，最后会报错’ValueError: list.remove(x): x not in list‘


#list()转换列表
n = list(range(11))
print(f"list():")           #不能直接print(list(range(0,11)),这样返回的结果是'list(range(0,11)'
print(n)

c = [v for v in range(0,11)]    #也可以使用列表推导式


#复制列表
a = n[:]