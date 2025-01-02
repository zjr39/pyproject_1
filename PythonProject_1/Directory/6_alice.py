from pathlib import Path

path = Path('6&7_alice.txt')
try:
    contents = path.read_text(encoding='utf-8')     # 如果系统的默认编码与要读取的文件的编码不一致，参数encoding必不可少
except FileNotFoundError:
    print(f"Sorry,the file {path} does not exist")
else:
    '''计算文本大致包含多少搞个单词'''
    words = contents.split()                        # spilt()将字符串分割转换为列表
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
finally:                                            # finally里面的代码总是会被执行
    print('Exit.')


'''split()的用法'''                                  # 文档字符串，绿色的比#显目
string = "apple,banana,cherry"
result = string.split(',')
print(result)
# 示例中输出结果为 ['apple', 'banana', 'cherry']

# maxsplit 参数：可以指定最大分割次数。例如：
string = "apple,banana,cherry,date"
result = string.split(',', maxsplit=2)
print(result)
# 这里指定 maxsplit=2，意味着最多只进行两次分割，得到的结果为
# ['apple', 'banana', 'cherry,date']，即从左到右只拆分了前两个逗号处，剩余部分作为最后一个元素保留在列表中。