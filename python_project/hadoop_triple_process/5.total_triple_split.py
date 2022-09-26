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

    total_triples = read_files("hadoop_data_process/total_triples.txt")
    relation_list = total_triples[:, 1].tolist()
    relation_num = len(list(set(relation_list)))
    print(relation_num)
    entity_list = total_triples[:, 0].tolist() + total_triples[:, 2].tolist()
    entity_num = len(list(set(entity_list)))
    print(entity_num)
    total_triples = list(total_triples)

    """relation and entity frequencey"""
    relation_frequency_path = "hadoop_data_process/relation_frequency.txt"
    entity_frequency_path = "hadoop_data_process/entity_frequency.txt"

    relation_frequency = read_files(relation_frequency_path)
    print("relation_frequency ", relation_frequency.shape)

    entity_frequency = read_files(entity_frequency_path)
    print("entity_frequency ", entity_frequency.shape)

    entity_frequency_dic = {}
    for i in range(len(entity_frequency)):
        entity_frequency_dic[entity_frequency[i][1]] = int(entity_frequency[i][2])

    relation_frequency_dic = {}
    for i in range(len(relation_frequency)):
        relation_frequency_dic[relation_frequency[i][1]] = int(relation_frequency[i][2])


    print("relation_total_frequency_dic", relation_frequency_dic)
    print("relation_total_frequency_dic", len(relation_frequency_dic))

    print("entity_frequency_dic", entity_frequency_dic)
    print("entity_frequency_dic", len(entity_frequency_dic))


    loop = 0
    train_triples = []
    train_entity_list = []
    train_relation_list = []

    train_relation_total = []
    train_entity_total = []
    while True:
        loop += 1
        total_triples_num = len(total_triples)
        index = np.random.random_integers(0, total_triples_num - 1)
        _triple = total_triples[index]

        h = _triple[0]
        r = _triple[1]
        t = _triple[2]

        if len(train_relation_total) >= relation_num and \
                len(train_entity_total) >= entity_num :
            print("out train triples")
            write_triples("hadoop_data_process/train_triples_part1.txt", train_triples)
            break
        else:
            if h not in train_entity_total or t not in train_entity_total or r not in train_relation_total:

                train_entity_list.append(h)
                train_entity_list.append(t)
                train_relation_list.append(r)

                train_triples.append(_triple)
                total_triples.pop(index)

        train_entity_total = list(set(train_entity_list))
        train_relation_total = list(set(train_relation_list))

        print("loop: ",loop)

    print("total triple left ", len(total_triples))

    write_triples("hadoop_data_process/total_triples_except_part1.txt", total_triples)
#
