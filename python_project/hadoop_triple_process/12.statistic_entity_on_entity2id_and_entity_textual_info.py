import numpy as np
import pandas as pd


def read_ID_Name_Mention_Time(entity_obj_path):

    f = open(entity_obj_path)

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
    X = np.array(x_obj)
    return X

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


if __name__ == "__main__":

    # entity_des2 = read_ID_Name_Mention_Time("./hadoop_with_other_components/total_entity_ID_Name_Mention_Time.txt")

    entity_des2 = pd.read_csv("./hadoop_with_other_components/total_entity_ID_Name_Mention_Time_adv.txt",sep="\t",header=None)
    entity_des2 = np.array(entity_des2)

    print(entity_des2.shape)
    entity_id = entity_des2[:,1]
    print(entity_id)

    entity_id_p = []
    for i in range(len(entity_id)):
        s = str(entity_id[i]).strip()
        entity_id_p.append(s)


    ne_entity2id_dic = {}
    for i in range(len(entity_id_p)):
        ne_entity2id_dic[entity_id_p[i]] = int(i)

    print("ne_entity2id_dic", len(ne_entity2id_dic))

    old_entity2id = read_files("./hadoop_with_other_components/total_entities.txt")
    print(old_entity2id.shape)
    old_entity2id = old_entity2id[:,0]

    # entity2id_dic, relation2id_dic = get_entity_relation_2id("./hadoop_data/entity2id.txt","./hadoop_data/relation2id.txt")

    s = 0
    no = 0
    no_entity = []
    for i in range(len(old_entity2id)):
        if old_entity2id[i] in entity_id_p:
            s += 1

        else:
            # print(old_entity2id[i])
            no +=1
            no_entity.append(old_entity2id[i])
    print(s)
    print(no)
    print(len(no_entity))

    write_entity("./hadoop_with_other_components/not_in_entity_textual_info_adv.txt", no_entity)




