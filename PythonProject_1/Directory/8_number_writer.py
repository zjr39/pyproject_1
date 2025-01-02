import json
from pathlib import Path

numbers = [2,3,5,7,11,13]
path = Path('8_number.json')
json_str = json.dumps(numbers)
path.write_text(json_str)


'''或者也可以用'''
with open ("8_number.json", "w") as f:
    json.dump(numbers,f)




"""
json.dump 和 json.dumps 的区别：
    一、定义和功能概述
        json.dump()是将 Python 对象转换为 JSON 格式的字符串，并将其写入到文件对象中。它主要用于将数据序列化并保存到文件中。
        json.dumps()则只是将 Python 对象转换为 JSON 格式的字符串，并不涉及文件写入操作，它返回一个 JSON 格式的字符串，可以用于在程序内部传递或者存储在其他非文件的数据结构中。
    二、参数方面
        json.dump()的参数：
            它的第一个参数是要序列化的 Python 对象，比如字典、列表等。第二个参数是一个文件对象（必须是可写的，如以w或wb模式打开的文件），用于存储序列化后的 JSON 数据。例如：
                import json
                data = {'name': 'John', 'age': 30}
                with open('data.json', 'w') as f:
                json.dump(data, f)
        json.dumps()的参数：
            它的主要参数是要转换的 Python 对象。例如：
                import json
                data = {'name': 'John', 'age': 30}
                json_str = json.dumps(data)
                print(json_str)
    三、返回值差异
        json.dump()没有返回转换后的 JSON 字符串，它的操作重点是将 JSON 数据写入文件。如果执行成功，它返回None。
        json.dumps()返回一个 JSON 格式的字符串。这个字符串可以用于后续的操作，如通过网络传输、存储在数据库中等。
    四、使用场景示例
        json.dump()使用场景：
            当你需要将程序中的数据结构（如配置信息、用户数据等）保存到本地文件，以便下次程序启动时读取使用，json.dump()是很好的选择。
        json.dumps()使用场景：
            如果你要将数据发送到网络服务器，通常需要先将数据转换为字符串格式。json.dumps()就可以用于将 Python 对象转换为 JSON 字符串，然后通过网络协议（如 HTTP）发送。
"""



"""
with open(file_name) as fileobject:
    一、基本语法和用途
        with open()是 Python 中用于打开文件的一种便捷方式。它的基本语法是with open(file_path, mode) as file_object:。
        其中file_path是要打开的文件的路径（可以是相对路径或绝对路径），mode是打开文件的模式，file_object是打开文件后得到的文件对象，通过这个对象可以对文件进行读取、写入等操作。
        它的主要用途是安全地打开和操作文件，当with代码块执行结束后，文件会自动关闭，无需手动调用file_object.close()方法，这样可以避免因为忘记关闭文件而导致的资源泄漏等问题。
    二、打开文件的模式（mode）
        1.读取模式（r）：
            这是默认模式。如果文件不存在，会抛出FileNotFoundError异常。例如，读取一个文本文件的内容：
                with open('example.txt', 'r') as file:
                    content = file.read()
                    print(content)
            在这里，file.read()会读取整个文件的内容并将其存储在content变量中，然后打印出来。
            如果文件较大，也可以使用file.readline()逐行读取文件内容，或者使用file.readlines()读取所有行并返回一个列表。
        2.写入模式（w）：
            如果文件不存在，会创建一个新文件；如果文件已经存在，则会清空文件内容并重新写入。例如，向一个文件中写入内容：
                with open('new_file.txt', 'w') as file:
                    file.write("This is a new file.")
            这里file.write()方法将字符串写入文件。需要注意的是，写入模式会覆盖原有文件内容。
        3.追加模式（a）：
            如果文件不存在，会创建一个新文件；如果文件已经存在，则会在文件末尾追加内容。例如：
                with open('log.txt', 'a') as file:
                    file.write("New log entry.")
            这样新的内容就会添加到log.txt文件的末尾。
    三、二进制模式（rb、wb、ab）：
        用于处理非文本文件，如图片、音频、视频等二进制文件。例如，读取一个二进制文件：
            with open('image.jpg', 'rb') as file:
                binary_data = file.read()
        或者写入一个二进制文件：
            with open('new_image.jpg', 'wb') as file:
                # 假设image_data是获取到的二进制数据
                file.write(image_data)
"""