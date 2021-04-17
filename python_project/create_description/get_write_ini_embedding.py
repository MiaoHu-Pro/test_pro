import torch
import numpy as np

import re
import math
import ast

from get_entity_description import read_file, read_train_set


# list -> pandas -> array
def write_initi_embedding(init_o, init_embedding, out_path, out_new_id):
    try:
        fobj = open(out_path, 'w')
        fobj_newi2 = open(out_new_id, 'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        for i in range(len(init_o)):
            _str = str(i) + '\t' + str(init_o[i]) + '\t' + str(list(init_embedding[i])) + '\n'
            fobj.writelines('%s' % _str)

            _str_id = str(i) + '\t' + str(init_o[i]) + '\n'
            fobj_newi2.writelines('%s' % _str_id)

        fobj.close()
        fobj_newi2.close()

    print('WRITE FILE DONE!')

def get_init_embedding(train_data,original_all_triples_path):

    print(train_data.shape)

    # obtain h
    h_array = train_data[:, 0:300]
    h_array = h_array.reshape((len(h_array), 1, len(h_array[0])))  # reshape
    # print(h_array.shape)
    # transform numpy to tensor
    h = torch.from_numpy(h_array)
    print(h.shape)
    # print(h[0,0,0:3])# 0.8655, 0.1105, 0.8599

    # obtain r
    r_array = train_data[:, 300:600]
    r_array = r_array.reshape((len(r_array), 1, len(r_array[0])))  # reshape

    r = torch.from_numpy(r_array)
    print(r.shape)
    # print(r[0,0,0:3])#

    # obtain t
    t_array = train_data[:, 600:900]
    t_array = t_array.reshape((len(t_array), 1, len(t_array[0])))  # reshape

    t = torch.from_numpy(t_array)
    print(t.shape)
    # print(t[0,0,0:3])#

    conv_input = torch.cat([h, r, t], 1)

    print(conv_input.shape)

    # obtain initial entity embedding, and relation embedding

    original_all_triples_path = original_all_triples_path

    X, relation_set, h_entity_set, t_entity_set, entityPair_set = read_train_set(original_all_triples_path)
    print('read_train_set over !')

    print(X.shape)  # (483142, 3)
    print(len(relation_set))  # 483142

    print('h_entity_set', len(set(h_entity_set)))  #

    print('t_entity_set', len(set(t_entity_set)))  #

    init_entity = []
    init_entity_embedding = []
    init_relation = []
    init_relation_embedding = []

    for i in range(len(X)):
        if h_entity_set[i] not in init_entity:
            init_entity.append(h_entity_set[i])
            print(i)
            # print("h_array[i][0]",h_array[i][0])
            init_entity_embedding.append(h_array[i][0])

        if t_entity_set[i] not in init_entity:
            init_entity.append(t_entity_set[i])
            init_entity_embedding.append(t_array[i][0])

    for i in range(len(X)):
        if relation_set[i] not in init_relation:
            init_relation.append(relation_set[i])
            init_relation_embedding.append(r_array[i][0])


    return init_entity,init_entity_embedding,init_relation,init_relation_embedding



def read_en_re_id(entity2id_path,relation2id_path):

    entity = []
    entity_id = []

    with open(entity2id_path) as f:
        for each_line in f:
            each_line = each_line.strip()
            if each_line:
                eachline_list = each_line.split('\t')
                if (len(eachline_list) != 2):
                    continue
                entity.append(eachline_list[0])
                entity_id.append(int(eachline_list[1]))

    # print(entity)
    f.close()

    relation = []
    relation_id = []

    with open(relation2id_path) as f:
            for each_line in f:
                each_line = each_line.strip()
                if each_line:
                    eachline_list = each_line.split('\t')
                    if (len(eachline_list) != 2):
                        continue
                    relation.append(eachline_list[0])
                    relation_id.append(int(eachline_list[1]))
    # print(relation)

    f.close()

    return entity,relation



def exchange_id_order_init_embedding(entity_order,entity_embs_path,relation_order,rel_embs_path):

    ini_ent = []
    ini_rel = []

    ini_ent_order = []
    ini_rel_order = []

    with open(rel_embs_path) as f:
        for each_line in f:
            each_line = each_line.strip()
            if each_line:
                eachline_list = each_line.split('\t')
                str_embed = eachline_list[2]
                ini_rel_order.append(eachline_list[1].strip())

                embed = ast.literal_eval(str_embed)  # str -> list
                ini_rel.append(embed)
    f.close()
    with open(entity_embs_path) as f:
        for each_line in f:
            each_line = each_line.strip()
            if each_line:
                eachline_list = each_line.split('\t')
                ini_ent_order.append(eachline_list[1].strip())
                embed = eachline_list[2]
                if embed:
                    each = embed.split(',')
                    elements = []
                    for n in each:
                        n = re.sub(r'[\[\]]', '', n)
                        if math.isnan(float(n)):
                            n = 0
                        elements.append(n)
                    ini_ent.append(elements)
    f.close()

    # print(ini_ent_order)
    # print(ini_rel_order)

    index_enti = []
    index_relation = []

    for i in entity_order:
        index = ini_ent_order.index(i)
        index_enti.append(index)

    for i in relation_order:
        index = ini_rel_order.index(i)
        index_relation.append(index)


    ini_ent = np.array(ini_ent, dtype=np.float32)
    ini_rel = np.array(ini_rel, dtype=np.float32)

    new_ini_ent = ini_ent[index_enti]

    new_ini_rel = ini_rel[index_relation]

    return new_ini_ent,new_ini_rel
    #获取顺序



if __name__ == "__main__":

    # load data
    train_data_path = '../data/FB15K/all_complex_triple2vector.txt'

    train_data = read_file(train_data_path)
    print(' train_complex_triple2vector over !')

    train_data = np.array(train_data)

    init_entity,init_entity_embedding,init_relation,init_relation_embedding = get_init_embedding(train_data)

    init_entity_embedding_out_path = '../data/FB15K/all_init_entity_embedding.txt'

    init_relation_embedding_out_path = '../data/FB15K/all_init_relation_embedding.txt'

    print(len(init_entity))  # 14951
    print(len(init_entity_embedding))

    print(len(init_relation))
    print(len(init_relation_embedding))  # 1345

    out_new_entity_id = './data/FB15K/new_entity2id.txt'
    out_new_relation_id = './data/FB15K/new_relation2id.txt'

    write_initi_embedding(init_entity, init_entity_embedding, init_entity_embedding_out_path, out_new_entity_id)
    write_initi_embedding(init_relation, init_relation_embedding, init_relation_embedding_out_path, out_new_relation_id)


    print("main over !")

    # 10 Feb tesk: get trainid.txt,text.txt valid.txt
