class Person:
    #当创建对象时，会走到__init__函数里面去
    def __init__(self,name,age,sex,te_chang,kou_tou_chan,zi_wo_jie_shao):
        print(name)
        print(age)
        print(sex)
        print(te_chang)
        print(kou_tou_chan)
        print(zi_wo_jie_shao)





cai_xu_kun = Person(
    name='蔡徐坤',
    age=23,
    sex='男',
    te_chang = ['唱','跳','rap','篮球'],
    kou_tou_chan = '你干嘛哎哟',
    zi_wo_jie_shao = '练习时长两年半'
)