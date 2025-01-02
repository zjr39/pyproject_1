alien_0={'color':'green','speed':'meidum','delete':'me'}


#删除键值对
del alien_0['delete']


#get()方法。第一个参数用于指定键，是必不可少的；第二个参数为当指定的键不存在时要返回的值，是可选的。
point_value = alien_0.get('point','No point value assigned.')
print(point_value)