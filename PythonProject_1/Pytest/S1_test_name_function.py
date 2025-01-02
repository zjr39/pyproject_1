"""测试文件必须以test_开头。运行pytest时，它将查找test_开头的文件并运行其中的测试"""
"""测试函数必须以test_打头。pytest将找出并运行所有以test_打头的函数。测试函数的名称应非常具体，因为不会调用，方便分析错误在哪。"""

from S1_name_function import get_formatted_name

def test_first_last_name():                         # test_开头
    '''能够正确处理像 Janis Joplin 这样的姓名吗?'''
    formatted_name = get_formatted_name('Janis','Joplin')
    assert formatted_name == 'Janis Joplin'         # 断言(assertion)就是声称满足特定的条件：这里声称formatted_name的值为'Janis Joplin'

def test_first_last_middle_name():
    '''能够正确处理像 Wolfhang Amadeus Mozart 这样的姓名吗？'''
    formatted_name = get_formatted_name('Wolfhang', 'Mozart','Amadeus')
    assert formatted_name == 'Wolfhang Amadeus Mozart'
# 很奇怪，后面再加一行才会运行两个测试，没有就只运行最后一个


"""
断言(assert)能测试包含任意可用条件语句
assert a == b
assert a != b
assert a                    断言a的布尔值为True
assert not a                断言a的布尔值为False
assert element in list
assert element not in list
"""