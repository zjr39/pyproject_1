from pathlib import Path

path = Path('1&2_pi_digits.txt')
contents = path.read_text()                       # 把文件变成可操作的字符串

pi_string = ''
for line in contents.splitlines():                # 简化代码。把字符串转变为分行的列表
    pi_string += line.strip()                     # 再把分行的列表转变为不分行的字符串

print(pi_string)
print(len(pi_string))                             # 打印长度


# 在读取文本时，python将所有的文本都解释为字符串。如果读取的是数，并且要作为数值使用，
# 就必须使用int()函数将其转换为整数，或者使用float()函数将其转换为浮点数。

# 如果包含100万位的大型文件，只打印到小数点后50位，只需做一步修改：
# print(f'{pi_string[:52]}')。    52是因为前面有两个元素 '3.'

path = Path('3_pi_million.txt')
contents_1 = path.read_text()

lines_1 = contents_1.splitlines()
pi_string_1 = ''
for line in lines_1:
    pi_string_1 += line.strip()

print(f'{pi_string[:52]}')                       # 52是因为前面有两个元素 '3.'
print(len(pi_string_1))