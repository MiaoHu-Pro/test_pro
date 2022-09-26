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
            _str = data[j][0] + '\t' + data[j][1] + '\t' + data[j][2] + '\t' + data[j][3] + '\n'

            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')


if __name__ == "__main__":

    total_triples = read_files("./hadoop_with_other_components/valid_and_test.txt")

    row, colum = total_triples.shape

    print(row, colum)

    time_table = sorted(total_triples[:, 3].tolist())

    print(time_table)

    """
    earliest time : 2006-02-01 02:54:35
    latest time: 2022-09-09 03:17:59

    
    """

    train_data = []
    test_data = []
    split_point = "2021-01-01 00:00:00"

    format_pattern = "%Y-%m-%d %H:%M:%S"

    for i in range(row):
        current = total_triples[i, 3]

        _current_time = datetime.strptime(current, format_pattern)

        _split_time = datetime.strptime(split_point, format_pattern)

        if _current_time > _split_time:
            test_data.append(total_triples[i].tolist())
        else:
            train_data.append(total_triples[i].tolist())

    print(len(test_data), len(train_data))

    write_triples_with_created_date("./hadoop_with_other_components/valid.txt", train_data)

    write_triples_with_created_date("./hadoop_with_other_components/test.txt", test_data)
