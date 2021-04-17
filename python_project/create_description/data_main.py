
import numpy as np
import pandas as pd

from read_json_entity2obj import read_json,define_entityObj

from get_entity_description import read_all_data,read_entity_obj,set_entity_obj,write_to_file_entity_obj,write_entity2vec,creat_nes_con_features,write_to_file

from get_write_ini_embedding import read_file,get_init_embedding,write_initi_embedding,read_en_re_id,exchange_id_order_init_embedding

"""
read_json_entity2obj -> data_utilities -> get_write_ini_embedding
Obtain new_init_entity_embedding and 
Obtain new_init_relation_embedding

"""

def get_entity2obj_from_json():
    pass
def get_all_triples_complex_vector():
    pass
def get_ent_rel_init_embedding():
    pass


if __name__ == "__main__":

    #
    # w_path = './FB15K/entity2Obj.txt'
    # path = './FB15K/entity2wikidata.json'
    # all_entity  = read_json(path)
    # print(len(all_entity))
    # entity2Obj_list = define_entityObj(all_entity) # return list
    # # 写文件
    # # wirte_file(enti_Ob_list,w_path)
    # print("read_json_entity2obj END\n")
    # print("============================================================\n")
    #
    # all_triples_path = './FB15K/all_triples.txt'
    #
    # set_entity_obj_path = './FB15K/all_entity_obj_set.txt'
    # entity2vec_path = './FB15K/all_entity2vec_set.txt'
    #
    # train_complex_triples_path = './FB15K/all_complex_triples.txt'
    # train_complex_triple2vector_path = './FB15K/all_complex_triple2vector.txt'
    #
    # # 首先获得entity2Obj，在kg_data_processing 中
    # entity_obj_path = './FB15K/entity2Obj.txt'
    #
    # X, relation_set, entity_set, entityPair_set = read_all_data(all_triples_path)
    #
    # print("read_train_set ->  over ! ")
    #
    # sub_x_obj = read_entity_obj(entity_obj_path) # 14515 entities have label and des , and about 436 has not desc...
    #
    # print("read_entity_obj ->  over ! ")
    #
    # print("len(entityPair_set)",len(entityPair_set))
    #
    # print(X.shape)
    #
    # relation_set = list(set(relation_set))
    # print("len relation_set",len(relation_set))
    # entity_set = list(set(entity_set))
    # print("len entity_set",len(entity_set))
    #
    # set_entity_obj = set_entity_obj(X,sub_x_obj,entity_set)
    # print("set_entity_obj ->  over ! ")
    #
    # write_to_file_entity_obj(set_entity_obj_path,set_entity_obj)
    #
    # write_entity2vec(entity2vec_path,set_entity_obj,entity_set) #entity_set 与 set_entity_obj对应
    #
    # print("write set_entity_obj  ->  over ! ")
    #
    # re = creat_nes_con_features(X,entity_set,set_entity_obj,train_complex_triple2vector_path)
    #
    # print("creat_nes_con_features ->  over ! ",re)
    #
    # # write_to_file(train_complex_triples_path,complex_triples_set)
    # # write_to_file(train_complex_triple2vector_path,triples2vector)
    # #
    # print("data_utilities END\n")
    # print("============================================================\n")


    # load data
    print("get_init_embedding")
    all_triples_path = './FB15K/all_triples.txt'
    train_data_path = './FB15K/all_complex_triple2vector.txt'

    train_data = read_file(train_data_path) #train_data = np.array(triples2vector)
    print(' train_complex_triple2vector over !')

    train_data = np.array(train_data)

    init_entity,init_entity_embedding,init_relation,init_relation_embedding = get_init_embedding(train_data,all_triples_path)

    init_entity_embedding_out_path = './FB15K/all_init_entity_embedding.txt'

    init_relation_embedding_out_path = './FB15K/all_init_relation_embedding.txt'

    print(len(init_entity))  # 14951
    print(len(init_entity_embedding))

    print(len(init_relation))
    print(len(init_relation_embedding))  # 1345

    out_new_entity_id = './FB15K/new_entity2id.txt'
    out_new_relation_id = './FB15K/new_relation2id.txt'

    write_initi_embedding(init_entity, init_entity_embedding, init_entity_embedding_out_path, out_new_entity_id)
    write_initi_embedding(init_relation, init_relation_embedding, init_relation_embedding_out_path, out_new_relation_id)


    print("main over !")

    # 10 Feb tesk: get trainid.txt,text.txt valid.txt

    print("get_write_ini_embedding END\n")
    print("============================================================\n")

    entity2id_path = './FB15K/entity2id.txt'
    relation2id_path = './FB15K/relation2id.txt'
    entity_embs_path = './FB15K/all_init_entity_embedding.txt'
    rel_embs_path = './FB15K/all_init_relation_embedding.txt'

    # entity_embs, rel_embs = read_init_embs(entity_embs_path,rel_embs_path)
    #
    entity_order,relation_order = read_en_re_id(entity2id_path,relation2id_path)

    entity_embs,rel_embs =  exchange_id_order_init_embedding(entity_order,entity_embs_path,relation_order,rel_embs_path)

    new_entity_embs_path = './FB15K/new_init_entity_embedding_300.txt'
    new_rel_embs_path = './FB15K/new_init_relation_embedding_300.txt'

    # obtain init entity and relation embedding
    np.savetxt(new_entity_embs_path,entity_embs,fmt='%f',delimiter=',')
    np.savetxt(new_rel_embs_path,rel_embs,fmt='%f',delimiter=',')

















