users = {
    '周周不复始':{
        '盗贼':{'暗夜精灵':{80:'达拉苏斯'}},
        '猎人':{'德莱尼':{70:'铁炉堡'}},
        '牧师':{'人类':{60:'暴风城'}}
    },
    '周而复始':{
        '萨满':{'牛头人':{50:'雷霆崖'}},
        '战士':{'兽人':{40:'奥格瑞玛'}},
        '法师':{'血精灵':{30:'银月城'}}
    }
}
for user_name,user_info_1 in users.items():                     # 名字

    print(f"\n{user_name}:")

    for zhi_ye,user_info_2 in user_info_1.items():              # 职业

        for zhong_zu,user_info_3 in user_info_2.items():        # 种族

            for level,location in user_info_3.items():          # 等级

                print(f"您的{level}级{zhong_zu}{zhi_ye}正在{location}和敌方火拼")