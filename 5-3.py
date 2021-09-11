score = input('please input your score:')
score = int(score)#必须转换成数字才可以比较
if  score>=90:
    print('you get a A')
elif  score>=80:
    print('you get a B')
elif  score>=70:
    print('you get a C')
elif  score>=60:
    print('you get a D')
else:
    print('you fail...')