


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


def write_triples(path,data):

    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][1]) + '\t' + str(data[k][0]) + '\t' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')

if __name__ == "__main__":

    train_data = read_files("./hadoop_data/train.txt")
    valid_data = read_files("./hadoop_data/valid.txt")
    test_data = read_files("./hadoop_data/test.txt")

    write_triples("./hadoop_data/test_relation_head_tail.txt",test_data)
    write_triples("./hadoop_data/valid_relation_head_tail.txt",valid_data)
    write_triples("./hadoop_data/train_relation_head_tail.txt",train_data)





