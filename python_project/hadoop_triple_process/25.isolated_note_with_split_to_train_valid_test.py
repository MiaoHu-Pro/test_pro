


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


if __name__ == "__main__":

    isolated_note_with_data = read_files("./hadoop_data_process/isolated_node_with_time.txt")

    row, colum = isolated_note_with_data.shape

    print(row, colum)

    time_table = sorted(isolated_note_with_data[:, 2].tolist())

    print(time_table)

    """
    earliest time : 2006-02-01 02:54:35
    latest time: 2022-08-31 03:17:59
    198 months
    """

    train_data = []
    valid_data = []
    test_data = []

    split_point1 = "2019-02-01 23:59:59"
    split_point2 = "2020-09-30 23:59:59"

    format_pattern = "%Y-%m-%d %H:%M:%S"

    for i in range(row):
        current = isolated_note_with_data[i, 2]

        _current_time = datetime.strptime(current, format_pattern)

        _split_time_1 = datetime.strptime(split_point1, format_pattern)

        _split_time_2 = datetime.strptime(split_point2, format_pattern)

        if _current_time <= _split_time_1:
            train_data.append(isolated_note_with_data[i].tolist())

        elif _split_time_1 < _current_time < _split_time_2:
            valid_data.append(isolated_note_with_data[i].tolist())

        elif _current_time > _split_time_2:
            test_data.append(isolated_note_with_data[i].tolist())

    print(len(test_data),len(valid_data), len(train_data))

    write_triples_with_created_date("./hadoop_data_process/train_isolated_node2id.txt", train_data)
    write_triples_with_created_date("./hadoop_data_process/valid_isolated_node2id.txt", valid_data)
    write_triples_with_created_date("./hadoop_data_process/test_isolated_node2id.txt", test_data)


