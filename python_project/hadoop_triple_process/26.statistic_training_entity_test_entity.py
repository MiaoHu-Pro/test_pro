
import os
from datetime import datetime

import numpy as np


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


def write_triples_with_created_date(out_path, data):
    ls = os.linesep
    num = len(data)

    try:
        fobj = open(out_path, 'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        fobj.writelines('%s\n' % num)
        for j in range(num):
            #
            _str = data[j][0] + '\t' + data[j][1] + '\n'

            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')

def write_data_2_id(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')
if __name__ == "__main__":

    training_entity = read_files("./hadoop_data_with_time/training_entity2id.txt")

    test_entity = read_files("./hadoop_data_with_time/test_entity2id.txt")

    training_entity_dic = {}

    for i in range(len(training_entity)):
       training_entity_dic[training_entity[i][0]] = training_entity[i][1]

    test_entity_in_train_set = []
    for i in range(len(test_entity)):
        _t = []
        if test_entity[i][0]  in training_entity_dic.keys():
            print(test_entity[i][0])
            print(test_entity[i][1])
            print(training_entity_dic.get(test_entity[i][0]))
            _t.append(test_entity[i][0])
            _t.append(training_entity_dic.get(test_entity[i][0]))
            test_entity_in_train_set.append(_t)

    write_data_2_id("./hadoop_data_with_time/test_entity_in_train.txt",test_entity_in_train_set)
