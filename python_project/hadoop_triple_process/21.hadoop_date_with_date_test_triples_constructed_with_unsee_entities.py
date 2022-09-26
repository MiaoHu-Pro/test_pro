
import os

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

def write_data_2_id(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\t' + str(data[k][2]) + '\t' + str(data[k][3]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')



if __name__ == "__main__":

    # train_data, train_times = load_quadruples('./Re_net_data/' + "WIKI", 'train.txt')
    # valid_data, valid_times = load_quadruples('./Re_net_data/' + "WIKI", 'valid.txt')
    test_data = read_files("./hadoop_data_with_time/test.txt")

    unsee_entity = read_files("./hadoop_data_with_time/test_entity_not_in_train.txt")
    unsee_entity = unsee_entity[:,0].tolist()

    unsee_entity_dict = {}
    for i in range(len(unsee_entity)):
        unsee_entity_dict[unsee_entity[i]] = int(i)


    print(len(unsee_entity))

    row, colum = test_data.shape

    # print(test_data)
    # print(test_times)
    print("unsee_entity_dict",unsee_entity_dict)
    test_triple_cpnstructed_with_unseen_entity = []
    n = 0
    m = 0
    for i in range(row):
        head = test_data[i][0]
        tail = test_data[i][2]
        print(i, head, tail)
        # if head in unsee_entity and tail in unsee_entity:
        if unsee_entity_dict.get(str(head)) and unsee_entity_dict.get(str(tail)):
            test_triple_cpnstructed_with_unseen_entity.append(test_data[i])
            n += 1
        else:
            m += 1
    print("how many test_triple_cpnstructed_with_unseen_entity: ", n)
    print("how man test with seen entity: ", m)

    write_data_2_id("hadoop_data_with_time/test_triple_constructed_with_unseen_entity.txt", test_triple_cpnstructed_with_unseen_entity)


"""
test : 1747

test_triple_constructed_with_unseen_entity:  1521
how man test with seen entity:  226

"""
