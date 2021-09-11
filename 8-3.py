others_bag = ['精灵弓 x1','箭矢 x20','金币 x100']
my_bag = ['咸鱼 x1']
print("others bag:",others_bag)
print("my bag:",my_bag)
def copy(bag1,bag2):
    for i in bag1:
        bag2.append(i)
    return bag2
my_bag = copy(others_bag,my_bag)
print('copy success:',my_bag)