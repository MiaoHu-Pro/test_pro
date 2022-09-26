
import numpy as np

def read_triple2id(rank_path):
    f = open(rank_path)
    f.readline()

    x_obj = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split(' ')

            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements
            x_obj.append(d)
    f.close()

    return np.array(x_obj)

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

def get_entity_relation_2id(entity_path,relation_path):

    relation = read_files(relation_path)
    entity = read_files(entity_path)

    entity2id_dic = {}
    for i in range(len(entity)):
        entity2id_dic[entity[i][0]] = int(entity[i][1])

    relation2id_dic = {}
    for i in range(len(relation)):
        relation2id_dic[relation[i][0]] = int(relation[i][1])

    # print(entity2id_dic,relation2id_dic)

    return entity2id_dic,relation2id_dic

def write_data_2_id(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + ' ' + str(data[k][1]) + ' ' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')

def obtain_trple2id(entity2id_dic,relation2id_dic,unseen_relation_inverse_test,unseen_relation_others_test):

    test_data = [unseen_relation_inverse_test,unseen_relation_others_test]
    test_data_name = ["unseen_relation_inverse_test","unseen_relation_others_test"]
    index = 0
    for _data in test_data:
        data2id = []
        print(_data)
        _data = np.array(_data)
        for i in range(len(_data)):
            _data2id = []
            _h = _data[i, 0]
            _r = _data[i, 1]
            _t = _data[i, 2]

            _h_id = entity2id_dic.get(_h)
            _t_id = entity2id_dic.get(_t)
            _r_id = relation2id_dic.get(_r)
            _data2id.append(_h_id)
            _data2id.append(_t_id)
            _data2id.append(_r_id)
            data2id.append(_data2id)

        write_data_2_id("./new_mxz_entity/new_mxz_entity_v1/" + test_data_name[index] +"2id.txt" ,data2id)
        index +=1


def write_triples_2_id(path, data):
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


if __name__ == "__main__":

    entity2id_path = "dataset_v2/entity2id.txt"
    relation2id_path = "dataset_v2/relation2id.txt"
    entity2id_dic,relation2id_dic = get_entity_relation_2id(entity2id_path,relation2id_path)

    print(relation2id_dic,len(relation2id_dic))
    print(entity2id_dic,len(entity2id_dic))

        # read triples

    file_name_list = ["./dataset_v2/test2id.txt",
                      "./dataset_v2/train2id.txt",
                      "./dataset_v2/valid2id.txt"]
    total_num = []
    total_relation = []
    total_entities = []
    total_triples = []
    for tem_rank in file_name_list:
        print(tem_rank)
        tem_triple_path = tem_rank

        _triples = read_triple2id(tem_triple_path)
        print(_triples.shape)
        _num = len(_triples)
        print("how many triples of"+tem_rank + ":",_num)
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

    print("total_relation :",len(list(set(total_relation))))
    print("total_entities :",len(list(set(total_entities))))

    print("how many triples:",np.sum(total_num))

    print("total_entities :",len(total_triples))


"""
total_relation : 32
total_entities : 6602
how many triples: 8864
total_entities : 8864
"""
