
import random_mode_test

def return_multiple():
    t = (1, 2, 3)
    return t

def yuanzu():
    print("---------yuanzu----------")
    #创建元组
    tup1 = 1, 2, 3
    print('--tup1--',tup1)

    # 嵌套元组
    tup2 = (1, 2, 3), (4, 5)
    print('--tup2--',tup2)

    #转换为元组，list->tuple, string->tuple
    l = [1, 2, 3]
    print(tuple(l))
    str = 'Hello ChinaHadoop'
    print(tuple(str))

    tup3 = tuple(str)
    print(tup3[4])

    print(tup1 + tup2)

    #
    # 函数返回多个值

    #(1, 2, 3)
    a, b, c = return_multiple()
    print(c)

    # 元组列表迭代
    tuple_lst = [(1, 2), (3, 4), (5, 6)]
    for x, y in tuple_lst:
        print( 'x + y',x + y)

def fun_liebiao():
    lst_1 = [1, 2, 3, 'a', 'b', (4, 5)]
    print(lst_1)

    lst_2 = range(1, 9)
    print(lst_2)

    tup = (1,3,4,5,6,7)
    list_3 = list(tup)
    print(list_3)

    lst_4 = range(10)
    print(lst_4)
    # 末尾添加
    #lst_4.append(11)
    #print(lst_4)

    # 指定位置插入
    #lst_4.insert(5, 12)
    #print(lst_4)

    # 删除指定位置的元素并返回
    #item = lst_4.pop(6)
    #print(item)
    #print(lst_4)
    # 删除指定的值，注意12在这里是“值”不是“位置”
    #lst_4.remove(12)
    #print(lst_4)

    lst_5 = range(10)
    #random.shuffle(lst_5)
    print(lst_5)

    lst_6 = ['Welcome', 'to', 'Python', 'Data', 'Analysis', 'Course']
    lst_6.sort();
    print('--list6--',lst_6);
#常用序列函数
def sequence_fun():

    lst_6 = ['Welcome', 'to', 'Python', 'Data', 'Analysis', 'Course']
    lst_6.sort();
    print('--list6--',lst_6);
    #enumerate ,拿到序列
    lst_6 = ['Welcome', 'to', 'Python', 'Data', 'Analysis', 'Course']  # (0, 'Welcome')
    for i, item in enumerate(lst_6):
        print('%i-%s' % (i, item))
    #字典
    str_dict = dict((i, item) for i, item in enumerate(lst_6))
    print('--str_dict--',str_dict)

    #zip
    lst_6 = ['Welcome', 'to', 'Python', 'Data', 'Analysis', 'Course']
    lst_7 = range(5)  # [0, 1, 2, 3, 4]
    lst_8 = ['a', 'b', 'c']
    zip_lst = zip(lst_6, lst_8, lst_7)
    print(zip_lst)

    #字典
    empty_dict = {}
    dict1 = {'a': 1, 2: 'b', '3': [1, 2, 3]}
    print(empty_dict)
    print(dict1)

    #键是4 值（4,5）
    dict1[4] = (4, 5)
    print(dict1)

    #删除元素
    del dict1[2]
    print(dict1)

    a_value = dict1.pop('a')
    print(a_value)
    print(dict1)

    #获取键、值列表
    print(dict1.keys())
    print(dict1.values())

    #合并字典
    dict2 = {6: 'new1', 5: 'news'}
    dict1.update(dict2)
    print(dict1)

    #通过多个列表创建字典
    #普通方法
    dict_3 = {}
    l1 = range(10)
    l2 = list(reversed(range(10))) #reversed 反序列
    for i1, i2 in zip(l1, l2):
        dict_3[i1] = i2
    print(dict_3)

    dict_4 = dict(zip(l1, l2))
    print(dict_4)

    #集合
    a = set(range(10))
    print(a)
    b = set(range(5, 15))
    print(b)

    print(a | b)
    print(a & b)
    print(a ^ b)
    print(a - b)

    #判断是否为子集、父集
    x = a.issubset(b)
    print(x)
    x = a.issuperset(b)
    print(x)



#列表推导式

def liebiao_fun():

    #列表推导式
    result2 = [i for i in range(10000) if i % 2 == 0];
    print(result2);

    str_lst = ['Welcome', 'to', 'Python', 'Data', 'Analysis', 'Course']
    result3 = [x.upper() for x in str_lst if len(x) > 4]
    print(result3)

    #字典推导式
    dict1 = {key: value for key, value in enumerate(reversed(range(10)))}
    print('字典推导式',dict1)

    #集合推导式
    set1 = {i for i in range(10)}
    print('集合推导式',set1)

    #嵌套推导式
    lists = [range(10), range(10, 20)]
    print('嵌套推导式',lists)

    evens = [item for lst in lists for item in lst if item % 2 == 0]
    print(evens)


if __name__ == '__main__':
    #yuanzu()
    #fun_liebiao()
    #sequence_fun()
    liebiao_fun()