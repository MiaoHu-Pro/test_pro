import os
from datetime import time
from datetime import datetime
import numpy as np
import pandas as pd


def read_files(rank_path):
    f = open(rank_path)
    f.readline()
    x_obj = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split('\t')

            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements
            x_obj.append(d)
    f.close()

    return np.array(x_obj)


def read_entity2obj(entity_obj_path):
    """
    14344(index) 	/m/0wsr(symbol) 	 Atlanta Falcons(label)	 American football team (description)
    :param entity_obj_path:
    :return:
    """
    f = open(entity_obj_path)

    x_obj = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split('\t')

            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements
            x_obj.append(d)

    f.close()
    X = np.array(x_obj)

    return X


def compare_two_time(first_time,second_time):

    # 日期格式话模版
    format_pattern = "%Y-%m-%d %H:%M:%S"

    # first_time = "2022-09-06 13:51:32"
    # second_time = datetime.now()
    # print(end_date) # datetime.datetime(2018, 10, 15, 11, 19, 52, 186250)
    # print(type(end_date)) # <type 'datetime.datetime'>

    # 将 'datetime.datetime' 类型时间通过格式化模式转换为 'str' 时间
    # second_time = second_time.strftime(format_pattern)
    # print(second_time, type(second_time)) # ('2018-10-15 11:21:44', <type 'str'>)

    # 将 'str' 时间通过格式化模式转化为 'datetime.datetime' 时间戳, 然后在进行比较
    _first_time = datetime.strptime(first_time, format_pattern)

    _second_time = datetime.strptime(second_time, format_pattern)

    if _first_time > _second_time:
        return str(_first_time)
    else:
        return str(_second_time)

    # strftime = datetime.strptime("2017-11-02", "%Y-%m-%d")
    # strftime2 = datetime.strptime("2017-01-04", "%Y-%m-%d")
    #
    # print("2017-11-02大于2017-01-04：",strftime>strftime2)

def write_entity2id(path,data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for key,value in data.items():

            _str = key + "\t" + str(value) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')
def write_triples_with_created_date(out_path,data):

    ls = os.linesep
    num = len(data)

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        fobj.writelines('%s\n' % num)
        for j in range(num):
            #
            _str = data[j][0] + '\t' + data[j][1] + '\t' + data[j][2]+ '\t' + data[j][3] + '\n'

            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')
def write_isolated_wntity_with_created_date(out_path,data):

    ls = os.linesep
    num = len(data)

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        fobj.writelines('%s\n' % num)
        for j in range(num):
            #
            _str = data[j][0] + '\t' + data[j][1] + '\t' + data[j][2] + '\n'

            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')


if __name__ == "__main__":

    isolated_note_array = read_files("./hadoop_data_process/isolated_node_2id.txt")

    print(isolated_note_array.shape)
    isolated_note = isolated_note_array[:,0].tolist()
    isolated_note_index = isolated_note_array[:,1].tolist()
    #
    entity_name_createdtime = read_entity2obj("./hadoop_data_process/ID_Name_create_date.txt")
    print(entity_name_createdtime.shape)

    entity_date = entity_name_createdtime[:,3].tolist()
    entity_name = entity_name_createdtime[:,1].tolist()

    entity_2_date = {}
    for i in range(len(entity_name)):
        entity_2_date[entity_name[i]] = entity_date[i]

    print(len(entity_2_date))

    isolated_note_2_date = []

    s = 0
    for i in range(len(isolated_note)):
        _iso_note2data = []
        if entity_2_date.get(isolated_note[i]):
            _iso_note2data.append(isolated_note[i])
            _iso_note2data.append(isolated_note_index[i])
            _iso_note2data.append(entity_2_date.get(isolated_note[i]))

            # print(entity_2_date.get(isolated_note[i]))
            s +=1
            # isolated_note_2_date[isolated_note[i]] = entity_2_date.get(isolated_note[i])
            isolated_note_2_date.append(_iso_note2data)

    print(s)
    write_isolated_wntity_with_created_date("./hadoop_data_process/isolated_node_with_time.txt",isolated_note_2_date)



