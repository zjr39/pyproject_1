class Users:
    def __init__(self,f_name,l_name,age):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = f"{self.f_name.title()} {self.l_name.title()}"     # 先定义全名
        self.age = age
        self.login_attempts = 0                                     # 尝试登录次数
        self.login_status = False                                   # 登录状态


    def greet_user(self):
        print(f"海内存知己，天涯若比邻。"
              f"欢迎您：{self.full_name}")

    def increment_login_attempts(self) -> '剩余登录次数' :            # -> 函数注释,注意是在冒号的前面
        self.login_attempts += 1
        remaining_login_attempts = 4 - self.login_attempts
        print(f"密码错误，还可尝试{remaining_login_attempts}次，"
              f"失败后将锁定30秒。")

    def reset_login_attempts(self) ->     '登录成功' :                    #登陆成功
        self.login_attempts = 0
        print(f"登录成功")

    def login(self) ->                    '登录':
        if self.login_status:
            print(f"您已经在登录状态，请勿重复操作。")
        else:
            self.login_status = True
            print(f'您已登录成功。')

    def log_out(self) ->                   '登出':
        if self.login_status:
            self.login_status = False
            print(f"正在退出...退出成功。")
        else:
            print(f"您已退出账号，请勿重复操作。")

    def run(self,seconds)   ->            '登录用时':                            # seconds 不用初始化定义
        if self.login_status:
            print(f"您本次登录用时{seconds}秒,击败了全国99%的用户！")
        else:
            print(f'一股神秘的力量低声说："请先登录..."')                 # 里面用"",外面就用''

    def __add__(self, other)    ->        'dunder':                # double underline 双下划线
        return f'{self.full_name}和{other.full_name}将联手合拍一部新电影，敬请期待！'     #这里可以直接用print

    def __str__(self)   ->                '修改字符串结果':
        return f"{self.age}岁的{self.full_name}"                    # 这里必须用return

    def __repr__(self) ->                 '__repr__':
        return f"{self.full_name}:{self.age}岁"



user_1 = Users('jacky','chen',60)               # User_1
user_1.greet_user()

print(f"\n————尝试登录次数————")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

print(f"\n————登录状态————")
user_1.login()                # 登录
user_1.run(0.01)              # 登录用时
user_1.login()                # 验证登录状态
user_1.log_out()              # 登出
user_1.log_out()              # 验证登出状态
user_1.run(0.01)              # 在登出状态验证登录用时


print(f'\n————dunder————')
user_2 = Users('Burce','Lee',40)               # User_2
print(user_1 + user_2)                                            # 添加两个用户的名字
print(user_1)                                                     # 修改后的字符串
print(repr(user_2))                                               # __repr__



print('\n———— Admin 子类 ————')
class Admin(Users):
    def __init__(self,f_name,l_name,age,)->   '添加特权新属性':
        super().__init__(f_name,l_name,age)
        self.privileges = Privileges()                      # 注意加()




class Privileges:
    def __init__(self,privileges = ["can add post","can delete post","can ban user"]):
        self.privileges = privileges

    def show_privileges(self)->     '显示管理员权限':
        print(f'您的管理权限有：')
        for privilege in self.privileges:                   # 必须是self.privileges
            print('-'+privilege)



admin = Admin('jerry','chen',21,)
admin.greet_user()
admin.privileges.show_privileges()

