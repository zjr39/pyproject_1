

def p_a(a,b):
    while a:                #当列表为空，停止循环
        c=a.pop()
        print(f"正在完成:{c}")
        b.append(c)

def p_b(b):
    print(f"\n已完成:")
    for d in b:
        print(d)

a=input('请输入第一项工作：')
b=input('请输入第二项工作：')
c=input('请输入第三项工作：')

a_list=[a,b,c]
b_list=[]


p_a(a_list,b_list)
p_b(b_list)


#每个函数都应只负责一项工作，优于使用一个函数完成两项工作
