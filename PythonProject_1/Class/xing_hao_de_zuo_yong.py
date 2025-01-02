'''一、重复功能'''
print('ha'*3)

'''二、打包'''
'''打包是将多个值捆绑到一个容器中，解包将容器中的值拿出来变成单独的变量。'''

'''1.一个*可以打包序列，当多个值传入带有*的变量时，这个变量就会变成一个列表。'''
numbers = [1,2,3,4,5]
first,*rest = numbers            # 接受任意数量的值变为列表
print(first)
print(rest)

'''2.一个*可以作为函数的位置实参，将传入的多个值打包为一个元组'''
def print_values(*args):
    for arg in args:
        print(arg)

print_values(1,2,3)

'''3.两个*可以作为关键字参数，将传入的多个值打包为一个字典'''
def example(**kwargs):
    for key, value in kwargs.items():           # 别忘了.items()
        print(f'{key} = {value}')

example(a=1,b=2,c=3)

'''三、解包'''
'''一个*可以解包序列'''
def greet(name,age):
    print(f"Hello {name},you are {age} years old.")

person = ('Alice',18)
greet(*person)

'''一个*可以序列合并'''
list = [1,2,3]
tuple = (4,5,6)
merged = [*list,*tuple]         # 这里可以()，也可以用[]
print(merged)

'''两个*可以解包字典'''
def create_profile(name,age,email):
    print(f'name:{name}')
    print(f'age:{age}')
    print(f'email:{email}')

option = {
    'name':'tony',                          # 逗号别忘了
    'age':18,
    'email':'tony@qq.com'
}

create_profile(**option)

'''两个*可以合并字典'''

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}
merged1 = {**dict1,**dict2}
print(merged1)