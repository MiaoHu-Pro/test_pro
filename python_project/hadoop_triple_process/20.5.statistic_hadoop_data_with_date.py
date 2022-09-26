import os

import numpy as np

def read_triple2id(rank_path):
    f = open(rank_path)
    f.readline()

    x_obj = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split(' ')

            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements
            x_obj.append(d)
    f.close()

    return np.array(x_obj)

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

def get_entity_relation_2id(entity_path,relation_path):

    relation = read_files(relation_path)
    entity = read_files(entity_path)

    entity2id_dic = {}
    for i in range(len(entity)):
        entity2id_dic[entity[i][0]] = int(entity[i][1])

    relation2id_dic = {}
    for i in range(len(relation)):
        relation2id_dic[relation[i][0]] = int(relation[i][1])

    # print(entity2id_dic,relation2id_dic)

    return entity2id_dic,relation2id_dic

def write_data_2_id(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + ' ' + str(data[k][1]) + ' ' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')

def obtain_trple2id(entity2id_dic,relation2id_dic,unseen_relation_inverse_test,unseen_relation_others_test):

    test_data = [unseen_relation_inverse_test,unseen_relation_others_test]
    test_data_name = ["unseen_relation_inverse_test","unseen_relation_others_test"]
    index = 0
    for _data in test_data:
        data2id = []
        print(_data)
        _data = np.array(_data)
        for i in range(len(_data)):
            _data2id = []
            _h = _data[i, 0]
            _r = _data[i, 1]
            _t = _data[i, 2]

            _h_id = entity2id_dic.get(_h)
            _t_id = entity2id_dic.get(_t)
            _r_id = relation2id_dic.get(_r)
            _data2id.append(_h_id)
            _data2id.append(_t_id)
            _data2id.append(_r_id)
            data2id.append(_data2id)

        write_data_2_id("./new_mxz_entity/new_mxz_entity_v1/" + test_data_name[index] +"2id.txt" ,data2id)
        index +=1


def write_triples_2_id(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\t' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')

def load_quadruples(inPath, fileName, fileName2=None, fileName3=None):
    with open(os.path.join(inPath, fileName), 'r') as fr:
        quadrupleList = []
        times = set()
        for line in fr:
            line_split = line.split()
            head = int(line_split[0])
            tail = int(line_split[2])
            rel = int(line_split[1])
            time = int(line_split[3])
            quadrupleList.append([head, rel, tail, time])
            times.add(time)
        # times = list(times)
        # times.sort()
    if fileName2 is not None:
        with open(os.path.join(inPath, fileName2), 'r') as fr:
            for line in fr:
                line_split = line.split()
                head = int(line_split[0])
                tail = int(line_split[2])
                rel = int(line_split[1])
                time = int(line_split[3])
                quadrupleList.append([head, rel, tail, time])
                times.add(time)

    if fileName3 is not None:
        with open(os.path.join(inPath, fileName3), 'r') as fr:
            for line in fr:
                line_split = line.split()
                head = int(line_split[0])
                tail = int(line_split[2])
                rel = int(line_split[1])
                time = int(line_split[3])
                quadrupleList.append([head, rel, tail, time])
                times.add(time)
    times = list(times)
    times.sort()

    return np.asarray(quadrupleList), np.asarray(times)

def write_entity(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')


if __name__ == "__main__":


    train_data = read_files('hadoop_data_with_time/train.txt')
    valid_data = read_files('hadoop_data_with_time/valid.txt')
    test_data = read_files('hadoop_data_with_time/test.txt')

    train_entity = list(set(list(set(train_data[:, 0].tolist())) +  list(set(train_data[:, 2].tolist()))))
    print("train entity:",len(train_entity))

    valid_entity = list(set(list(set(valid_data[:, 0].tolist())) +  list(set(valid_data[:, 2].tolist()))))
    print("valid entity:",len(valid_entity))

    test_entity = list(set(list(set(test_data[:, 0].tolist())) +  list(set(test_data[:, 2].tolist()))))
    print("test entity:",len(test_entity))

    unseen_entity = []
    for i in range(len(test_entity)):
        if test_entity[i] not in train_entity:
            unseen_entity.append(test_entity[i])
    print("how many test entity dose not in train set",len(unseen_entity))

    write_entity("./hadoop_data_with_time/test_entity_not_in_train.txt", unseen_entity)

    print("relation : ")

    train_relation = list(set(train_data[:, 1].tolist()))
    valid_relation = list(set(valid_data[:, 1].tolist()))
    test_relation = list(set(test_data[:, 1].tolist()))

    print("train relation:",len(train_relation))
    # print("valid relation:",len(valid_relation))
    print("test relation:",len(test_relation))


    unseen_relation = []
    for i in range(len(test_relation)):
        if test_relation[i] not in train_relation:
            unseen_relation.append(test_relation[i])
    print("how many test relation dose not in train set: ",len(unseen_relation))
