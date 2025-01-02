from temp_1 import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('jacky','chen',5000)
    return employee


def test_give_defalut_raise(employee):
    '''测试默认加薪'''
    employee.give_raise()
    assert employee.annual_salary == 10000

def test_give_custom_raise(employee):
    '''测试制定加薪10000'''
    employee.give_raise(10000)
    assert employee.annual_salary == 15000

def test_name(employee):
    '''测试姓名输出'''
    assert employee.name == 'Jacky Chen'
