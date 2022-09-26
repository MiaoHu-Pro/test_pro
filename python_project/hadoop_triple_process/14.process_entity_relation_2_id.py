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

def write_entity_relation2id(path,data):

    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = data[k][1] + '\t' + data[k][0] + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')


if __name__ == "__main__":

    entity_frequenct = "./dataset_v3/entity_frequency.txt"

    entity = read_files(entity_frequenct)

    print(entity.shape)

    relation_frequenct = "./dataset_v3/relation_frequency.txt"

    relation = read_files(relation_frequenct)

    print(relation.shape)
    write_entity_relation2id("./dataset_v3/entity2id.txt",entity)
    write_entity_relation2id("./dataset_v3/relation2id.txt",relation)


