

def show_msg(a):
    print('\n请确认您的信息')
    for b in a:
        print(b)

def send_msg(a,b):
    while a:
        e=a.pop()
        b.append(e)
    print()
    b.reverse()
    print(b)




a=input('您的生日时间是：')
b=input('您的酒店位置是：')
c=input('请输入到达酒店的交通工具：')
d=input('请输入交通工具的线路：')

s_msg=[a,b,c,d]
sd_msg=[]

show_msg(s_msg)
send_msg(s_msg,sd_msg)


