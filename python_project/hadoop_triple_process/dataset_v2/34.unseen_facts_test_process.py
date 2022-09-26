import numpy as np

"""
1. read unseen_relation_test.txt
2. Divided into two categories according to unseen_relation_test_1892forward.txt

    unseen_relation_test_inverse.txt --> unseen_relation_test_inverse2id.txt
    unseen_relation_test_others.txt  --> unseen_relation_test_others2id.txt

3. serialization (turn unseen_relation_test_inverse into unseen_relation_test_inverse2id.txt)

"""

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

def split_unseen_relation_test(unseen_relation_test_path):

    unseen_relation_test = read_files(unseen_relation_test_path)

    print(unseen_relation_test.shape)

    u_relation_test_inverse = read_files("test.txt")
    u_relation_test_others = read_files("valid.txt")

    relation2id_inverse_dic = {}
    for i in range(len(u_relation_test_inverse)):
        relation2id_inverse_dic[u_relation_test_inverse[i][0]] = int(u_relation_test_inverse[i][1])


    relation2id_others_dic = {}
    for i in range(len(u_relation_test_others)):
        relation2id_others_dic[u_relation_test_others[i][0]] = int(u_relation_test_others[i][1])

    print(relation2id_inverse_dic)
    print(relation2id_others_dic)

    unseen_relation_inverse_test = []
    unseen_relation_others_test = []

    for i in range(len(unseen_relation_test)):

        if relation2id_inverse_dic.get(unseen_relation_test[i][1]):
            unseen_relation_inverse_test.append(unseen_relation_test[i].tolist())
        else:
            unseen_relation_others_test.append(unseen_relation_test[i].tolist())

    print("unseen_relation_inverse_test", len(unseen_relation_inverse_test))
    print("unseen_relation_others_test", len(unseen_relation_others_test))

    from utilities import write_triples_2_id
    write_triples_2_id("unseen_relation_inverse_test.txt",unseen_relation_inverse_test)
    write_triples_2_id("unseen_relation_others_test.txt",unseen_relation_others_test)


    return unseen_relation_inverse_test, unseen_relation_others_test


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

        write_data_2_id(test_data_name[index] +"2id.txt" ,data2id)
        index +=1




if __name__ == "__main__":

    entity2id_path = "entity2id.txt"
    relation2id_path = "relation2id.txt"
    entity2id_dic,relation2id_dic = get_entity_relation_2id(entity2id_path,relation2id_path)

    unseen_relation_test_path = "/Users/miaoxuzhi/Desktop/DSA8030/dsa8030_project/ALL/relationship.csv"
    unseen_relation_inverse_test, unseen_relation_others_test = split_unseen_relation_test(unseen_relation_test_path)
    obtain_trple2id(entity2id_dic,relation2id_dic,unseen_relation_inverse_test,unseen_relation_others_test)





