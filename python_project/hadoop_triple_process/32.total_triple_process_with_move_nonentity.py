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


def write_triples(path,data):

    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)
        print("the number of lines: ",num)
        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\t' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')


if __name__ == "__main__":

    total_triples = read_files("./hadoop_with_other_components/total_triples.txt")

    row, colum = total_triples.shape

    print(row, colum)

    nan_entity = ['Wiki Page','Page']
    total_triples_adv = []
    s = 0
    for i in range(row):

        _triple = []
        head = total_triples[i][0]
        rel = total_triples[i][1]
        tail = total_triples[i][2]

        if head in nan_entity or tail in nan_entity:
            print(total_triples[i])
            s += 1
            print(s)
        else:
            total_triples_adv.append(total_triples[i])


    print("total s ", s)
    write_triples("./hadoop_with_other_components/total_triples_adv.txt",total_triples_adv)
