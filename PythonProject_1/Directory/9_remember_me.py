from pathlib import Path
import json

'''重构:把代码划分为数个函数，每个函数都执行单一而清晰的任务。'''

def get_stored_info(path):
    '''如果存储了数据，就获取它'''
    if path.exists:                             # 如果指定的文件夹存在，exists()方法返回True,否则返回False
        contents = path.read_text()
        info = json.loads(contents)
        return info
    else:
        return None                             # 函数要么返回预期的值，要么返回None，这让我们可以使用函数的返回值做简单的测试。

def get_new_info(path):
    '''提示用户输入用户名、年龄、地址'''
    username = input('What is your name?')      # 函数里面的变量是临时变量/局部变量，可在其他函数中使用相同函数名。
    age = input('How old are you?')
    location = input('Where you live?')
    dict = {'username':username,'age':age,'location':location}
    contents = json.dumps(dict)
    path.write_text(contents)
    return dict

def greet_user():
    '''问候用户，并打印其信息'''
    path = Path('9_username.json')
    info = get_stored_info(path)
    if info:
        verify = input(f'Is this your username {info['username']}?(yes or no)')
        if verify == 'yes':
            print(f"Welcome back,{info['username']}!.Today is your {info['age']} years old birthday."
                  f"We will send a present to CQ")
        else:
            info = get_new_info(path)
            print(f"We will remember you when you come back,{info['username']}!")
    else:
        info = get_new_info(path)
        print(f"We will remember you when you come back,{info['username']}!")

# path = Path('9_username.json')                # 忽略这两行，我只是为了存储新的信息
# get_new_info(path)
greet_user()


"""
源代码：
from pathlib import Path
import json

def greet_user():
    path = Path(9_username.json)
    if path.exists:
        contents = path.read_text()
        usename = json.load(contents)
        print(f"Welcome back,{username}!")
    else:
        username = input('What is your name?')
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you come back,{username}!")

greet_user()
"""