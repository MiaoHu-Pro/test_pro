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

def write_entity2id(path,data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for key,value in data.items():

            _str = key + "\t" + str(value) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')


if __name__ == "__main__":

    # files_name = ['hadoop_common_total_triples.txt', 'HBASE_total_triplet.txt', 'HDFS_total_triplet.txt',
    #               'HIVE_total_triplet.txt',
    #               'MAPREDUCE_total_triplet.txt', 'PIG_total_triplet.txt', 'YARN_total_triplet.txt']

    files_name = ['total_triples_adv.txt']

    total_entities = []
    total_relations = []
    total_triples = []
    for file_name in files_name:
        print("file name:", file_name)

        _triples = read_files("./hadoop_with_other_components/" + file_name)

        head = _triples[:, 0]
        relation = _triples[:, 1]
        tail = _triples[:, 2]

        _entities = list(set(list(set(head)) + list(set(tail))))
        _relations = list(set(relation))

        total_entities += _entities
        total_relations += _relations

        total_entities = list(set(total_entities))
        total_relations = list(set(total_relations))

        total_triples += list(_triples)

    print("len(total_triples): ", len(total_triples))
    print("len(total_entities): ", len(total_entities))
    print("len(total_relations): ", len(total_relations))

    total_entities_dic = {}

    for i in range(len(total_entities)):
        total_entities_dic[total_entities[i]] = int(i)

    total_relations_dic = {}

    for i in range(len(total_relations)):
        total_relations_dic[total_relations[i]] = int(i)



    # write_triples("./hadoop_with_other_components/total_triples_adv2.txt",total_triples)
    # write_entity2id("./hadoop_with_other_components/total_entities_adv.txt",total_entities_dic)

    write_entity2id("./hadoop_with_other_components/total_relations_adv.txt",total_relations_dic)

    # write_entity("./hadoop_with_other_components/total_relations_adv.txt",total_relations)
