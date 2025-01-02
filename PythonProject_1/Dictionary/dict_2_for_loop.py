favorite_languages = {
    'amy':'python',
    'bob':'jave',
    'claire':'c',
    'dick':'python',
}


#遍历键值对
for name,language in favorite_languages.items():       # 字典是一个无序的键值对结果，item()返回一个包含字典中所有键值对的视图,
    print(f"{name.title()}'s loves {language} most.")  # 这个视图是一个可迭代对象，其中每个元素都是一个包含键和值的元组.


#遍历所有键      .keys()会返回一个列表，其中包含字典中的所有键
friends = ['phil','sarah','claire']
print(f"\n遍历所有键.keys()：")
for name in favorite_languages.keys():
    print(f"Hi,{name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()},I see your love {language}!')

  
#按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    n = name                                    #忽略它，只是为了演示sorted()


#遍历所有值      .values()
print(f"\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):           #set()方法可排除列表中重复的元素，并剩余元素创建一个集合。
    print(language.title())
