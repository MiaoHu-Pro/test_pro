"""
Obtain entity description and relation description

entity description:
entity name || entity mention || entity neighbours

relation description:
relation mention, which is a relationship between head and tail || one of head-entity neighbour || one of tail neighbour

"""
from get_entity_description import read_all_data,read_entity_obj,set_entity_obj,read_entity2id
from get_triples_description import read_ent_rel_2id,read_data2id
'''
1. combine train.txt,valid.txt, and test.txt
2. obtain each entity neighbours : get_entity_description.py
3. create relation description 
    1-obtain relation
    2-obtain head and tail
    3-combine: 
    relation, which is between head and tail.
    head has a relation of r with h1
    tail has a relation of r with t1.
'''

if __name__ == "__main__":

    """
    生成实体的描述和id向量
    """

    train_path = './FB15K/all_triples.txt'
    set_entity_obj_path = './FB15K/all_entity_description_3.txt'
    entity2vec_path = './FB15K/all_entity2id_randomly_vector_3.txt'

    train_complex_triples_path = './FB15K/all_complex_triples.txt'
    train_complex_triple2vector_path = './FB15K/all_complex_triple2vector.txt'

    # 首先获得entity2Obj，在kg_data_processing 中
    entity_obj_path = './FB15K/entity2Obj.txt'

    X, relation_set, entity_set, entityPair_set = read_all_data(train_path)

    sub_x_obj = read_entity_obj(entity_obj_path) # 14515 entities have label and des , and about 436 has not desc...

    # 获取entity id
    entity2id_path = "./FB15K/entity2id.txt"
    entity_id_read_file = read_entity2id(entity2id_path)
    entity_id_set = entity_id_read_file[:,0].tolist()

    entity_description_obj, all_entity_description_list, new_word_bag,word_bag_dic,pre_word_embedding = set_entity_obj(X,sub_x_obj,entity_id_set)

    number_of_entity = len(entity_description_obj)

    print(number_of_entity)
    for i in range(number_of_entity):
        tmp_en = entity_description_obj[i]
        entity_str = tmp_en.id + '\t' + tmp_en.symb + '\t' + tmp_en.label + '\t' + tmp_en.description
        print(entity_str)
        entity_des = tmp_en.get_entity_description()
        print("entity_des :\n ",entity_des)

        print("all_entity_description_list :\n",all_entity_description_list[i])
        import time
        time.sleep(2)


    """
    Obtain entity2id ,relation2id, and train2id. 
    """

    entity2id_path = "./FB15K/entity2id.txt"
    relation2id_path = "./FB15K/relation2id.txt"
    train_id_path = "./FB15K/train2id.txt"

    entity2id = read_ent_rel_2id(entity2id_path)
    relation2id = read_ent_rel_2id(relation2id_path)
    train2id = train_id = read_data2id(train_id_path)

    """obtain triples description"""
    # get_triples_description(train2id, relation2id, entity_description_obj)
    # get_triples_description(train2id, relation2id, entity_description_obj, word_bag_dic, pre_word_embedding)


