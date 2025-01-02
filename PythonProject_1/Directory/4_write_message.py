from pathlib import Path

path = Path('4_programming.txt')
path.write_text('I love programming.')
# write_text()接受单个实参，即写入文件的字符串
# Python 只能将字符串写入文本文件。如果存储数值数据，必须先使用函数str()将其转换为字符串格式
# 当指定的文件路径对应的文件不存在时，write_text() 方法会自动创建该文件
# 注意：write_text()会写入文本内容并覆盖原有内容（若文件已存在）


# 写入多行：
contents = 'I love programming.\n'
contents += 'I love creating new game.\n'
contents += 'I also love working with data.'
path.write_text(contents)
# 如果一个个调用write_text()会被覆盖，所以用一个变量替代要写入的字符串。