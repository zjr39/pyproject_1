from pathlib import Path
import json

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

path = Path('9_username.json')
print(get_stored_info(path))