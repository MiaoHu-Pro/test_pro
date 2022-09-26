


import numpy as np
def write_triples(path,data):

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


if __name__ == "__main__":

    train_triples_part1 = read_files("hadoop_data_process/train_triples_part1.txt")

    train_triples_part2 = read_files("hadoop_data_process/train_triples_part2.txt")

    train_triples_part1 = list(train_triples_part1)
    train_triples_part2 = list(train_triples_part2)
    train = train_triples_part2 + train_triples_part1
    write_triples("hadoop_data_process/train.txt", train)
