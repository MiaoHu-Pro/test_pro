import numpy as np
import pandas as pd


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



def get_sorted_list(d, reverse=False):

    """
        d = {"a":1 , "b":3, "c":2}
        得到排好序的列表

        dict_items([('a', 1), ('b', 3), ('c', 2)])

        reverse是排序规则是否反过来，默认是升序
        reverse = False 升序
        reverse = True 降序
        d_list
       [('a', 1), ('c', 2), ('b', 3)]
	"""
    return sorted(d.items(), key=lambda x:x[1], reverse=reverse)

if __name__ == "__main__":

    entity_des = pd.read_csv("hadoop_data_process/entity_textual_info.txt", sep="\t")
    entity_des = np.array(entity_des)

    print(entity_des.shape)
    entity_id = entity_des[:,0]
    print(entity_id)

    entity_id = list(set(entity_id))
    print(len(entity_id))

    entity_id_p = []
    for i in range(len(entity_id)):
        s = str(entity_id[i]).strip()
        entity_id_p.append(s)

    # print("entity_id_p:",entity_id_p)

    all_entity2id_dic = {}
    for i in range(len(entity_id_p)):
        all_entity2id_dic[entity_id_p[i]] = int(i)

    print("all_entity2id_dic", len(all_entity2id_dic))

    old_entity2id = read_files("hadoop_data_process/entity2id.txt")
    print(old_entity2id.shape)
    old_entity_id = old_entity2id[:,0]
    old_entity_index = old_entity2id[:,1]
    #
    # entity2id_dic, relation2id_dic = get_entity_relation_2id("./hadoop_data_process/entity2id.txt","./hadoop_data_process/relation2id.txt")

    # s = 0
    # no = 0
    # no_entity = []
    # for i in range(len(old_entity2id)):
    #     if old_entity2id[i] in entity_id_p:
    #         s += 1
    #
    #     else:
    #         # print(old_entity2id[i])
    #         no +=1
    #         no_entity.append(old_entity2id[i])
    # print(s)
    # print(no)
    # print(len(no_entity))
    #
    # write_entity("hadoop_data_process/not_in_entity_textual_info.txt", no_entity)

    # print(entity2id_dic)

    isolated_point = {}

    entity2id_dic = {}
    for i in range(len(old_entity_id)):
        entity2id_dic[old_entity_id[i]] = old_entity_index[i]

    print("entity2id_dic",entity2id_dic)
    print("entity2id_dic",len(entity2id_dic))

    s = 1
    for i in all_entity2id_dic.keys():
        if entity2id_dic.get(i):
            pass
            # print(entity2id_dic.get(entity_id[i]))

        else:
            isolated_point[i] = 12248 + s
            entity2id_dic[i] = 12248 + s

            s = s + 1

    print(len(entity2id_dic))
    print(entity2id_dic)

    # entity_2id = get_sorted_list(entity2id_dic)


    # write_entity2id("./hadoop_data_process/entity2id_all.txt", entity2id_dic)
    write_entity2id("./hadoop_data_process/isolated_note.txt", isolated_point)
