# Section 1

from pathlib import Path                      # 从pathlib模块导入Path类。Path对象指向一个文件，可以让你在使用文件之前核实它是否存在，
                                              # 读取文件的内容，以及将新数据写入文件。

path = Path('1&2_pi_digits.txt')                  # Path要大写，参数要全称，包括文件后缀名
contents = path.read_text()                   # .read_text() 将该文件的全部内容作为一个字符串返回
contents = contents.rstrip()                  # .read_text()在文件末尾会返回一个空字符串，这个空字符串会被显示为一个空行。也就是说比原文件多一个空行

print(contents)


# 相对文件路径：要么将数据存储在程序文件所在的目录中，要么将其存储在程序文件所在目录的下一个文件夹
# 比如：程序文件所在目录python_work，子目录text_file,文件名filename.txt
# path = Path('text_file/filename.txt')

# 绝对文件路径：可读取系统中任何地方的文件，以系统的根文件夹为起点
# path = Path('/home/eric/data_files/text_files/filename')


print('\n使用.splitline()方法访问文件中的各行:')
lines = contents.splitlines()                 # .splitline() 返回一个列表，包含文件中所有的行
for line in lines:
    print(line)