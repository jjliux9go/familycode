money = 100
price1 = 10
price2 = 20
price3 = 30
while True:
    print('''
    ===================================
    | 1.苹果10元 2.荔枝20元 3.榴莲30元 |
    |                                 |
    | 输入数字购买，输入q或者没钱了退出  |
    ===================================
    ''')
    choice = input('数字选择您的商品：')
    if choice == '1':
        print('你买了苹果，消费10元。')
        money-= price1
        print('剩余金额： ',money,'元')
    elif choice == '2':
        print('你买了荔枝，消费20元。')
        money-= price2
        print('剩余金额： ',money,'元')
    elif choice == '3':
        print('你买了榴莲，消费30元。')
        money-= price3
        print('剩余金额： ',money,'元') 
    if money<price1 or choice=='n':
        print('感谢你的购物，再见。')
        break