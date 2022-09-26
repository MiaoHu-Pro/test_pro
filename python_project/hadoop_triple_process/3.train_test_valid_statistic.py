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

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\t' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')

def write_entity_relation_frequency(path, data):
    num = len(data)
    file = open(path, 'w')
    file.writelines('%s\n' % num)
    i = 0
    for e in data:
        file.write(str(i) + '\t' + str(e[0]) + '\t' + str(e[1]) + '\n')
        i += 1

    file.close()

def static_frequency(dic_path, data):
    d = data
    c = dict.fromkeys(d, 0)
    for x in d:
        c[x] += 1
    sorted_x = sorted(c.items(), key=lambda d: d[1], reverse=True)

    write_entity_relation_frequency(path=dic_path, data=sorted_x)

if __name__ == "__main__":

    file_name_list = ["./dataset_v1/valid.txt",
                      "./dataset_v1/train.txt",
                      "./dataset_v1/test.txt"]
    total_num = []
    total_relation = []
    total_entities = []
    total_triples = []
    for tem_rank in file_name_list:
        print(tem_rank)
        tem_triple_path = tem_rank

        _triples = read_files(tem_triple_path)
        print(_triples.shape)
        _num = len(_triples)
        print("how many triples of" + tem_rank + ":",_num)
        total_num.append(_num)

        _relation = _triples[:, 1].tolist()
        print("how many of relation: ", len(list(set(_relation))))

        total_relation += list(set(_relation))
        total_relation = list(set(total_relation))

        _entity = _triples[:, 0].tolist() + _triples[:, 2].tolist()
        print("how many of entity: ", len(list(set(_entity))))

        total_entities += list(set(_entity))
        total_entities = list(set(total_entities))

        total_triples += _triples.tolist()



        static_frequency( tem_rank+ "_relation_frequency.txt", _relation)
        static_frequency( tem_rank+ "_entity_frequency.txt", _entity)

    print("total_relation :",len(list(set(total_relation))))
    print("total_entities :",len(list(set(total_entities))))

    print("how many triples:",np.sum(total_num))

    print("total_entities :",len(total_triples))

    # write_triples("./dataset_v1/total_triples.txt",total_triples)
