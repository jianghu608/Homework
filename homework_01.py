def demo(place, name):
    place = input('输入一个地名：')
    name = input('输入一个人名：')

    # 方法1 
    print(f'{place}很美，{name}想去看看')
   
    # 方法2
    print("{0}很美，{1}想去看看".format(place, name))

    # 方法3
    print(place + '很美，' + name + '想去看看')

    # 方法4
    print(place, '很美，', name, '想去看看', sep='')

    # 方法5（不好）
    print(place,end = '')
    print('很美，', end = '')
    print(name, end = '')
    print('想去看看')

demo("", "")