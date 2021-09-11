person0 = {'name':0,'level':0,'roletype':0}
person1 = {'name':0,'level':0,'roletype':0}
person2 = {'name':0,'level':0,'roletype':0}
all_person = [person0,person1,person2]
for i in range(3):
    all_person[i]['name'] = input('输入当前角色名称：')
    all_person[i]['level'] = input('当前等级：')
    all_person[i]['roletype'] = input('角色职业:')
    print('-------------------------------\n')
for i in all_person:
    print('================================')
    print(i['name'],i['level'],i['roletype'])