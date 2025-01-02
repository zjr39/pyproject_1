# 嵌套循环 nested_loop


#   * 在列表中存储字典 *
print('在列表中存储字典：')
aliens = []                                                 #创建一个存储外星人的空列表
for alien_number in range(30):                              #创建30个绿色的外星人
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:                                    #修改绿色外星人为黄色外星人
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:                                    #显示前5个外星人
    print(alien)
print('...')
print(f"Total number of aliens:{len(aliens)}")              #显示创建了多少个外星人



#   * 在字典中存储列表_pizza *
print(f"\n\n在字典中存储列表_pizza：")

pizza = {'crust':'thick','toppings':['mushrooms','extra cheese']}
print(f"You orderd a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print('-'+ topping)


#   * 在字典中存储列表_languages *
print(f"\n\n在字典中存储列表_languages：")

favorite_languages = {
    'amy':['python','rust'],
    'bob':['jave'],
    'claire':['c#','rust'],
    'dick':['python','c++']
}
for name,languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t-{language.title()}")



#   * 在字典中存储字典 *
print(f"\n\n在字典中存储字典：")
users = {
    'Leonardo':{
        'first':'Leonardo',
        'last':'DiCaprio',
        'location':'Ameica'
    },
    'Jacky':{
        'first':'jacky',
        'last':'chen',
        'location':'China'
    }
}
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()
    print(f"\tFull name:{full_name}")
    print(f"Location:{location}")



