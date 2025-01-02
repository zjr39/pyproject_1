import pytest
from S2_servey import AnonymousSurvey

@pytest.fixture         #当测试函数的一个形参与应用了装饰器@pytest.fixture的函数(夹具)同名时，将自动运行夹具，并将夹具法返回的值传给测试函数。
def language_survey():
    '''一个可供所有测试函数使用的 AnonymousSurvey 实例'''
    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    reponses = ['English','Spanish','Mandarin']
    for response in reponses:
        language_survey.store_response(response)

    for response in reponses:
        assert response in language_survey.responses

"""
夹具(fixture)可帮助我们搭建测试环境。要创建夹具，可编写一个使用装饰器@pytest.fixture装饰的函数。
装饰器(decorator)是放在函数定义前面的指令。在运行函数前，Python将该指令应用于函数，以修改函数代码的行为。详情参考class文件夹。
当测试函数的一个形参与应用了装饰器@pytest.fixture的函数(夹具)同名时，将自动运行夹具，并将夹具法返回的值传给测试函数
"""