from pathlib import Path
import json

path = Path('8_number.json')
contents = path.read_text()                     # 将文件内容作为json格式的字符串返回
numbers = json.loads(contents)                  # 将json格式的字符串作为参数，返回一个python对象
print(numbers)


'''也可以用'''
with open ('8_number.json','r')as f:
    data = json.load(f)
    print(data)




"""
json.load 和 json.loads 的区别:
    json.load() 用于从文件对象中读取 JSON 数据并进行解析。
        with open('data.json', 'r') as file:
            data = json.load(file)
    json.loads() 用于从字符串中解析 JSON 数据。
        json_str = '{"key": "value"}'
        data = json.loads(json_str)
        
    应用场景差异
        json.load():
            当你需要从磁盘上的 JSON 文件或者其他类似文件流的数据源（如网络套接字读取的 JSON 数据存储在文件对象中）中加载 JSON 数据时，
            就会使用json.load()。这种方式更适合处理较大的 JSON 数据集，因为它可以直接从文件中逐步读取和解析数据，而不需要一次性将整个文件内容读取到内存中作为一个大字符串。
        json.loads()
            当你已经从某个地方获取到了一个 JSON 格式的字符串（比如从数据库中读取的 JSON 字符串，或者从网络请求的响应文本中提取的 JSON 部分），
            并且想要将其转换为 Python 对象进行处理时，json.loads()就非常方便。不过，如果字符串非常大，可能会占用较多内存，因为它是一次性将整个字符串解析为 Python 对象。

"""