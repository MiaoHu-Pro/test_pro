'''
Created on Dec 3, 2016

@author: Bin Liang
'''

from datetime import datetime
import  copy


def run_main1():
    """
        main function
    """
    chinese_str = 'Python数据分析'
    print (chinese_str)

    other_str = 'naïve'
    print (other_str)

    print("-----------")

def run_main2():
    # 普通方法
    result1 = []
    result2 = []
    for i in range(10000):
        if i % 2 == 0:
            result1.append(i)
        else:
            result2.append(i)


    print(result1)
    print(result2)

    print("-----------")
def run_main3():
    print ('%d %s cost me $%.2f.' %(2, 'books', 21.227))

    s_val = '3.1415926'
    print('string value: %s' % s_val)
    f_val = float(s_val)
    print('float value: %f' % f_val)
    i_val = int(f_val)
    print('int value: %i' % i_val)

    print("-----------")

def run_main4():
    dt = datetime(2016, 12, 3, 15, 0, 0)
    print (dt.year ,dt.month, dt.day)
    print("-----------")
    # range xrage

    #xrange(1, 20, 2)


    # for 循环
    l = range(20)  # [0, 1, 2, ..., 19]
    for i in l:
        if i % 2 == 0:
            continue
        if i == 15:
            break
        print(i)
    print("-----------")
    #while
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    print(sum)
    print("-----------")
    #列表传递
    l_1 = [1, 2, 3]
    l_2 = l_1
    l_1.append(100)

    print(l_1)
    print(l_2)
    print("-----------")

    lst1 = [1,2,3,4,5,6,7,8,9]
    fun2(lst1)

#列表传递是引用传递
#值传递，就是赋值
def fun2(lst):
    print("------fun2-----")
    lst[0] = 5
    print(lst)

    lst1 = range(5)
    print(lst1)

def copy_test():
    print("------copy_test-----")
    a = [[1, 2, 3], [4, 5, 6]]
    b = a

    #浅拷贝
    c = copy.copy(a)
    # 深拷贝
    d = copy.deepcopy(a)

    print('a-id:', id(a))
    print('b-id:', id(b))
    #c 、d 是拷贝，不是指向同一个地址
    print('c-id:', id(c))
    print('d-id:', id(d))

    a.append(15)
    a[1][2] = 10
    print('processed...')
    print(a)
    print(b)
    print(c)
    print(d)

if __name__ == '__main__':

    run_main1()
    #run_main2()
    #run_main3()
    #run_main4()
    #copy_test()
