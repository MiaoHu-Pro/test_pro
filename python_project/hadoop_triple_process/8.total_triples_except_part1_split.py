




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

    total_triples = read_files("hadoop_data_process/total_triples_except_part1.txt")

    loop = 0
    train_triples = []
    train_entity_list = []
    train_relation_list = []

    train_relation_total = []
    train_entity_total = []

    total_triples = list(total_triples)

    while True:
        loop += 1
        total_triples_num = len(total_triples)
        index = np.random.random_integers(0, total_triples_num - 1)
        _triple = total_triples[index]

        h = _triple[0]
        r = _triple[1]
        t = _triple[2]

        if len(train_triples) >= 6826:
            print("out train triples")
            write_triples("hadoop_data_process/train_triples_part2.txt", train_triples)

            left_num = len(total_triples)
            split_point = 0.5
            valid = total_triples[0:int(left_num*split_point)]
            test = total_triples[int(left_num*split_point):]

            write_triples("hadoop_data_process/test.txt", valid)
            write_triples("hadoop_data_process/valid.txt", test)

            break
        else:
            train_triples.append(_triple)
            total_triples.pop(index)


        print("loop: ",loop)

#
