def make_album(singer_name,album_name,album_count=None):
    album={'singer_name':singer_name,'album_name':album_name}
    if album_count:
        album['album_count']=album_count#这里要加引号
    return album
    
    

while True:
    print('\n输入q退出')
    s_name=input('输入歌手名字：')
    if s_name=='q':
        break
    a_name=input('输入专辑名字：')
    if a_name=='q':
        break
    a_count=input('输入专辑歌曲数：')
    if a_count=='q':
        break

    m_album=make_album(s_name,a_name,a_count)#这里不用引号
    print()
    print(m_album)

     
