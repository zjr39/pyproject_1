class Employee:
    def __init__(self,f_name,l_name,annual_salary):
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = annual_salary      # 不用int也行
        # n = f"{self.f_name} {self.l_name}"
        self.name = f"{self.f_name} {self.l_name}".title()

    def give_raise(self,increment=5000):
        '''默认加薪5000，可指定加薪数额'''
        self.annual_salary += increment
