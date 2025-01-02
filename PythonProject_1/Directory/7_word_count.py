from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少单词"""
    try:
        contents = path.read_text(encoding='utf8')
    except FileNotFoundError:
        print(f"Sorry,the file {path} does not exist")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

file_names = ['6&7_alice.txt','6&7_moby_dict.txt','little_women.txt']
for file_name in file_names:
    path = Path(file_name)
    count_words(path)


'''
静默失败:
    except FileNotFoundError:
        pass
使程序在发生异常时保持静默，继续运行
'''
