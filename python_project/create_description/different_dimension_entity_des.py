import sys

import numpy as np
import pandas as pd
from numpy.core._multiarray_umath import ndarray

from utilities import Enti, Rela, write_to_file, entity_text_process, relation_text_process
from text_analytics.text_analytics.text_analytics import text_analytics
import ast
from get_word2vector import read_word_bag
import torch
import torchtext

ta = text_analytics()


def read_ent_rel_2id(data_id_paht):
    data = pd.read_csv(data_id_paht)  #
    data = np.array(data)
    data_id = []
    for i in range(len(data)):
        _tmp = data[i][0]
        tmp = _tmp.split('\t')
        if tmp:
            id_list = []
            for s in tmp:
                id_list.append(s)
            data_id.append(id_list)
    data = np.array(data_id)
    return data


def read_data2id_partly(data_id_paht):
    data = pd.read_csv(data_id_paht)  #
    data = np.array(data)
    data_id = []
    for i in range(len(data)):
        if i == 10000:
            break
        _tmp = data[i][0]
        # tmp = _tmp.split(' ')
        # if tmp:
        #     id_list = []
        #     for s in tmp:
        #         id_list.append(s)
        #     data_id.append(id_list)
        data_id.append(_tmp)
    data = np.array(data_id)
    return data


def read_data2id(data_id_paht):
    data = pd.read_csv(data_id_paht)  #
    data = np.array(data)
    data_id = []
    for i in range(len(data)):
        _tmp = data[i][0]
        tmp = _tmp.split(' ')
        if tmp:
            id_list = []
            for s in tmp:
                id_list.append(s)
            data_id.append(id_list)
    data = np.array(data_id)
    return data


def read_entity_description(entity_description):
    """
    14344(index) 	/m/0wsr(symbol) 	 Atlanta Falcons(label)	 American football team (description)
    :param entity_obj_path:
    :return:
    """
    f = open(entity_description)

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
    return x_obj


def set_relation_description_obj(relation):
    print("set_relation_description_obj ... ")

    relation_name = relation[:, 0]
    rel_obj_set = []
    relation_description_list = []
    for i in range(len(relation_name)):
        relation_description_list.append(str(relation_name[i]))

    relation_description_word_list = relation_text_process(relation_description_list)

    for i in range(len(relation_name)):
        rel2vector = np.random.uniform(-0.5, 0.5, 50)
        rel = Rela(_id=i, _name=relation_name[i], _mention=None, _neighbours=None, _rel2vec=rel2vector,
                   _rel_des_word_list=relation_description_word_list[i])
        rel_obj_set.append(rel)

    return rel_obj_set, relation_description_word_list


def set_entity_description_obj(entity_des):
    all_entity_description_word_list = []
    entity_description_list = []

    for i in range(len(entity_des)):

        print(i)

        entity_id = entity_des[i][0]
        symbol = entity_des[i][1]
        name = entity_des[i][2]
        mention = entity_des[i][3]
        import ast
        neighbours_data = ast.literal_eval(entity_des[i][4])  # "list" -> list

        if len(neighbours_data) == 0:
            neighbours = ['the entity has not neighbours']
        else:
            neighbours = neighbours_data

        id2vector = np.random.uniform(-0.5, 0.5, 50)

        en_des = str(symbol) + '$' + str(name) + '$' + str(mention) + '$' + str(neighbours)
        entity_des_word_list = entity_text_process(en_des)  # get entity des 's word list

        entity = Enti(_id=entity_id, _symbal=symbol, _label=name, _description=mention, _neighbours=neighbours,
                      _entity2vec=id2vector, _entity_des_word_list=entity_des_word_list)

        en_des_word_list = entity.get_entity_description()
        all_entity_description_word_list.append(en_des_word_list)

        entity_description_list.append(entity)

    print(len(all_entity_description_word_list))

    return entity_description_list, all_entity_description_word_list


def get_word_bag(train2id, relation2id, entity_description_obj):
    print("get_triples_description - begin ... \n")

    """
    重要，不要删除
    train2id : the index of train data
    relation2id: the index of relation
    entity_description_obj : entity object which contains id, symbol, name, description, neighbours.
    word_bag : the number of words of relation and entity
    pre_word_embedding: the word-vector of all words
    return: pre-description embedding.
    """

    # number_of_entity = len(entity_description_obj)
    # print(number_of_entity)
    # all_entity_description_list = []
    # for i in range(number_of_entity):
    #     tmp_en = entity_description_obj[i]
    #
    #     entity_str = tmp_en.id + '\t' + tmp_en.symb + '\t' + tmp_en.label + '\t' + tmp_en.description
    #     print(entity_str)
    #
    #     en_des_word_list = tmp_en.get_entity_description()
    #
    #     all_entity_description_list.append(en_des_word_list)

    word_list = ["NULL"]
    head_description_list = []
    # relation_description_list = []
    # tail_description_list = []

    for i in range(len(train2id)):
        print(i)

        # head_description_list = []

        # print(i," --> ",train2id[i],"\n")
        # if i == 10:
        #     print("i = 10 break !")
        #     break

        head_index = int(train2id[i][0])
        tail_index = int(train2id[i][1])
        relation_index = int(train2id[i][2])

        head_obj = entity_description_obj[head_index]

        tail_obj = entity_description_obj[tail_index]

        rela_des = relation2id[relation_index][0]

        # head_description = head_obj.get_des()
        relation_description = str(
            rela_des) + ', ' + 'which is between ' + head_obj.symb + ' and ' + tail_obj.symb + ';' \
                               + head_obj.get_random_neighbour() + ';' + tail_obj.get_random_neighbour()
        # tail_description = tail_obj.get_des()

        # text_process(head_description)

        # print(head_description,"\n")
        # print(relation_description,"\n")
        # print(tail_description,"\n")
        # print("===================")

        """
        obtain entity and relation description represented by word
        """
        # head_description_word_list = entity_text_process(head_description)
        # relation_description_word_list = relation_text_process(relation_description)
        # tail_description_word_list = entity_text_process(tail_description)
        #
        head_description_word_list = head_obj.get_entity_description()
        relation_description_word_list = relation_text_process(relation_description)
        tail_description_word_list = tail_obj.get_entity_description()

        """ create word-bag , I have obtain word list , and obtain each word embedding using glove"""
        word_list += head_description_word_list
        word_list += relation_description_word_list
        word_list += tail_description_word_list
        word_list = list(set(word_list))

        """ next , all words become vector using World2vector 
            将获取的head_description_word_list，relation_description_word_list，tail_description_word_list
            通过word词模型，变成向量,然后使用LSTM进行编码
            from get_word2vector import get_word2vec 
        """

        # print("\n head description pre-vector... \n")
        # print(head_description_word_list)
        # print(np.array(pre_word_embedding[[word_bag[x] for x in head_description_word_list]]))
        #
        # print("\n relation description pre-vector... \n")
        # print(relation_description_word_list)
        # print(np.array(pre_word_embedding[[word_bag[x] for x in relation_description_word_list]]))
        #
        # print("\n tail description pre-vector... \n")
        # print(tail_description_word_list)
        # print(np.array(pre_word_embedding[[word_bag[x] for x in tail_description_word_list]]))

        # get sentence embedding

        head_description_list.append(head_description_word_list)
        # relation_description_list.append(relation_description_word_list)
        # tail_description_list.append(tail_description_word_list)

        # print("head_description_list",head_description_list)

    # get_sentence_init_embedding(pre_word_embedding,word_list,head_description_list)

    write_to_file("./FB15K/word_bag_2.txt", word_list)


def create_train2id_100000e():
    train2id_path = "./FB15K/test2id.txt"
    train2id_100000 = read_data2id_partly(train2id_path)
    print(len(train2id_100000))
    print(train2id_100000[0])
    write_to_file('./FB15K/test2id_10000.txt', train2id_100000)
    # import time
    # time.sleep(10)


def load_golve_vec(word_list, _dim):
    glove = torchtext.vocab.GloVe(name="6B", dim=_dim)

    print("load bin vec \n")
    word_vectors = {}

    for w in glove.itos:
        if w in word_list:
            word_vectors[w] = glove[w]

    return word_vectors


def word2vector(word_dict, dim):
    """

    """
    print("Word to vector ... \n")
    # word2vector
    word_to_idx = word_dict  # 数据集中所有的单词

    pretrained_embeddings = np.random.uniform(-0.5, 0.5, (len(word_dict), dim))

    # word2vec = load_w2v_vec('./data/GoogleNews-vectors-negative300.bin', word_to_idx)
    word2vec = load_golve_vec(word_to_idx, dim)

    for word, vector in word2vec.items():  # 初始化每个词

        pretrained_embeddings[word_to_idx[word]] = vector

    # 打印测试
    # print("NULL -> ",word_to_idx['NULL'],pretrained_embeddings[word_to_idx['NULL']])
    # print("contemporary -> ",pretrained_embeddings[30080])
    # print("the - > ",pretrained_embeddings[12104])
    # print("the - > ",pretrained_embeddings[word_to_idx['the']])

    # singer_index = word_to_idx['singer']
    # print(singer_index)
    # print("singer - > ",pretrained_embeddings[singer_index])
    # print("bryan - > ",pretrained_embeddings[25286])
    #
    pretrained_embeddings = torch.as_tensor(pretrained_embeddings)
    return pretrained_embeddings


def get_des_embedding(pre_embeddings, word_bag, sentence_set):
    print("Begin get_des_embedding ... ")

    init_embedding = []
    for i in range(len(sentence_set)):
        word_index = [word_bag[x] for x in sentence_set[i]]

        tmp_embedding = pre_embeddings[word_index]
        # print(tmp_embedding)
        init_mean_embedding = np.mean(np.array(tmp_embedding), axis=0).tolist()
        # print("init_embedding mean :",init_mean_embedding)
        init_embedding.append(init_mean_embedding)

    print("Finish get_des_embedding ...")
    return init_embedding


def obtain_dif_dim_vector(entity_description_obj, all_entity_description_list, relation_description_obj,
                          all_relation_description_list):
    """
    id = 50
    create 50d,100d,200d,300d description
    1. id50_des0
    2. id50_des50
    3. id50_des100
    4. id50_des200
    5. id50_des300

    """

    word_bag_path = "./FB15K/word_bag.txt"
    word_bag, all_word_dic = read_word_bag(word_bag_path)  # obtain word bag

    dim_l = [0, 50, 100, 200, 300]

    for d in dim_l:
        if d == 0:
            print("dim: ", d)
            # entity

            entity_description_embedding = []
            for i in range(len(entity_description_obj)):
                vec = entity_description_obj[i].entity2vec
                entity_description_embedding.append(vec)

            entity_des_embedding = np.array(entity_description_embedding)
            # relation
            # 随机生成50向量
            relation_description_embedding = []
            for j in range(len(relation_description_obj)):
                vec = relation_description_obj[j].rel2vec
                relation_description_embedding.append(vec)
            #
            relation_des_embedding = np.array(relation_description_embedding)

            np.savetxt('./FB15K/new_init_entity_embedding_id50_des0.txt', entity_des_embedding, fmt='%.5f', delimiter=',')
            np.savetxt('./FB15K/new_init_relation_embedding_id50_des0.txt', relation_des_embedding, fmt='%.5f',
                       delimiter=',')

        else:
            print("dim: ", d)
            pre_word_embedding = word2vector(all_word_dic, d)

            # obtain des embedding
            entity_description_embedding = get_des_embedding(pre_word_embedding, all_word_dic,
                                                             all_entity_description_list)
            relation_description_embedding = get_des_embedding(pre_word_embedding, all_word_dic,
                                                               all_relation_description_list)

            # cat id embedding and des embedding
            entity_id_des_embedding = []
            for i in range(len(entity_description_obj)):
                vec = entity_description_obj[i].entity2vec.tolist()
                vec = vec + entity_description_embedding[i]
                entity_id_des_embedding.append(vec)

            relation_id_des_embedding = []
            for i in range(len(relation_description_obj)):
                vec = relation_description_obj[i].rel2vec.tolist()
                vec = vec + relation_description_embedding[i]
                relation_id_des_embedding.append(vec)

            print(len(entity_id_des_embedding))
            print(len(relation_id_des_embedding))

            x_en_id_des_em = np.array(entity_id_des_embedding)
            x_rel_id_des_em = np.array(relation_id_des_embedding)

            print(x_en_id_des_em.shape)
            print(x_rel_id_des_em.shape)

            np.savetxt('./FB15K/new_init_entity_embedding_id50_des' + str(d) + '.txt', x_en_id_des_em, fmt='%.5f',
                       delimiter=',')
            np.savetxt('./FB15K/new_init_relation_embedding_id50_des' + str(d) + '.txt', x_rel_id_des_em, fmt='%.5f',
                       delimiter=',')
            print("d: %d over" % d)

    print("obtain_dif_dim_vector... over ...")


if __name__ == "__main__":
    """
    Obtain entity2id ,relation2id, and train2id. (25 Mar)
    """
    entity2id_path = "./FB15K/entity2id.txt"
    relation2id_path = "./FB15K/relation2id.txt"
    train_id_path = "./FB15K/train2id.txt"

    entity2id = read_ent_rel_2id(entity2id_path)
    relation2id = read_ent_rel_2id(relation2id_path)

    # create_train2id_100000e()
    #

    """obtain entity description"""
    entity_description = "./FB15K/all_entity_description_4.txt"
    entity_description = read_entity_description(entity_description)  # read original entity description
    entity_description_obj, all_entity_description_list = set_entity_description_obj(
        entity_description)  # set entity object

    """obtain relation description"""
    relation_description_obj, all_relation_description_list = set_relation_description_obj(relation2id)

    obtain_dif_dim_vector(entity_description_obj, all_entity_description_list, relation_description_obj,
                          all_relation_description_list)
