#类就是所有对象的共同特征抽取出来，实现代码复用。类是对象的模版
class Person:
    #当创建对象时，会走到__init__函数里面去
    def __init__(self,name,age,sex,te_chang,kou_tou_chan,zi_wo_jie_shao):
        self.name = name              #cai_xu_kun.name=name
        self.age = age                #self是对象本身
        self.sex = sex
        self.te_chang = te_chang
        self.kou_tou_chan = kou_tou_chan
        self.zi_wo_jie_shao = zi_wo_jie_shao

    def ktc(self):          #ktc(cai_xu_kun)
        print(self.kou_tou_chan)              #不能与kou_tou_chan同名

    def zwjs(self):
        print(self.zi_wo_jie_shao)

cai_xu_kun = Person(
    name='蔡徐坤',
    age=23,
    sex='男',
    te_chang = ['唱','跳','rap','篮球'],
    kou_tou_chan = '你干嘛哎哟',
    zi_wo_jie_shao = '练习时长两年半'
)
print(cai_xu_kun.name)
cai_xu_kun.ktc()
cai_xu_kun.zwjs()


#用self 可以确保在多个实例中，每个实例都能正确地访问和操作属于自己的数据
# ->主要用于函数注释,注意是在冒号的前面
# 快速注释：ctrl + /