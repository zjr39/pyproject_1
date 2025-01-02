file_name = '3_pi_million.txt'

with open(file_name) as file_object:        # 自动处理文件的关闭操作，无需您手动调用 close() 方法。在这个语句块中，您可以对打开的文件 file_object 进行读取、写入等操作.
    lines = file_object.readline()          # .readline()读取文件的所有行，并将每一行作为一个字符串元素存储在一个列表 lines 中。

pi_str = ''
for line in lines:
    pi_str += line.strip()

birthday = input('请输入您的生日:')
if birthday in pi_str:
    print('你的生日出现在圆周率中！')
else:
    print('你的生日没用出现在圆周率当中')

# read()专属于with open,返回字符串:
#       with open(file_name) as file_object:
#           contens = file_object.read()

# read_text()专属于pathlib,返回字符串:
#       from pathlib import Path
#       path = Path(file_name)
#       contents = path.read_text()


# splitlines()作用于字符串，返回字符串中所有行的列表
# readlines()作用于文件，返回文件中所有行的列表
# 注意是readlines,如果是readline则只读取一行，返回字符串。每次调用 readline() 都会顺序读取下一行，直到文件末尾。

# 简略版：
print('简略版：')
file_name = '3_pi_million.txt'

with open(file_name) as file_object:
    contents = file_object.read()

birthday = input('请输入您的生日:')
if birthday in contents:
    print('你的生日出现在圆周率中！')
else:
    print('你的生日没用出现在圆周率当中')