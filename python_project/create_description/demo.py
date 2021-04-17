#! /usr/bin/python3
# -*-coding:utf-8-*-
import sys

import numpy as np
import pandas as pd
from text_analytics.text_analytics.text_analytics import text_analytics
import ast
ta = text_analytics()
import torchtext
glove = torchtext.vocab.GloVe(name="6B", dim=300)
import time

"""
technology：
Tensor.detach().numpy().tolist() -> tensor become list
"[1,2,3,4,5]" --> [1,2,3,4,5]
1.
import ast
data_new = ast.literal_eval(data)
2.
answer_start = eval(answer_start)
:return: str_list -> list
"""

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

def relation_text_process():
    """
    given a relation , which was transformed into a word vector
    """
    rel_str = "/film/actor/film./film/performance/film, which is between /m/07nznf and /m/014lc_;/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/award with /m/02g3ft;/m/014lc_ has a relationship of /film/film/release_date_s./film/film_regional_release_date/film_release_region with /m/0f8l9c"

    rel_str = rel_str.split(";")

    relation_mention = rel_str[0]
    relation_neighbours = rel_str[1:]

    relation_mention_list = relation_mention.split(" ")
    print(relation_mention_list)
    relation_mention = ta.clean(relation_mention_list[0])

    relation_mention += relation_mention_list[1:]

    print(relation_mention)

    print("---------------")

    # str = ta.clean(str)
    # relation_mention = ta.clean(rel_str[0])
    # print(str[2])
    # print(ta.clean(ast.literal_eval(str[3])[0]))

    # li = ast.literal_eval(rel_str[1])
    # print("neighbours : ",len(li))


    #
    # entity_description_list.append(entity_symbol)
    #
    # entity_description_list += entity_name
    #
    # entity_description_list += entity_des

    relation_description_list = []
    relation_description_list += relation_mention
    neighbours_li = []
    #
    for i in range(len(relation_neighbours)):

        re_list = relation_neighbours[i].split(" ") # 分解每个邻居
        # print(re_list)
        sub_re_list = re_list[1:-1]
        # print(sub_re_list)
        w_list = [re_list[0]] # 取头实体
        for j in range(len(sub_re_list)):
            w_list += ta.clean(sub_re_list[j])

        w_list.append(re_list[-1]) # 取尾巴实体
        print(i)
        print(w_list)
        relation_description_list += w_list
        neighbours_li.append(w_list)

    # print(neighbours_li)
    print("neighbours : ", len(neighbours_li))

    print(relation_description_list)
    print(len(relation_description_list))

def entity_text_process():
    """
    given a entity , which was transformed into a word vector
    """

    ent_str = "/m/07nznf;Bryan Singer;American film director, writer and producer;" \
          "['/m/07nznf has a relationship of /people/person/nationality with /m/09c7w0', " \
          "'/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/nominated_for with /m/04p5cr', " \
          "'/m/07nznf has a relationship of /medicine/notable_person_with_medical_condition/condition with /m/029sk', " \
          "'/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award_nominee with /m/08xwck', " \
          "'/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/nominated_for with /m/016fyc', " \
          "'/m/07nznf has a relationship of /film/actor/film./film/performance/film with /m/014lc_', " \
          "'/m/07nznf has a relationship of /film/producer/films_executive_produced with /m/01qb5d', " \
          "'/m/07nznf has a relationship of /people/person/profession with /m/0dxtg', " \
          "'/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/01qb5d', " \
          "'/m/07nznf has a relationship of /base/schemastaging/person_extra/net_worth./measurement_unit/dated_money_value/currency with /m/09nqf', " \
          "'/m/07nznf has a relationship of /film/director/film with /m/02qhlwd', " \
          "'/m/07nznf has a relationship of /people/person/education./education/education/institution with /m/065y4w7', '/m/07nznf has a relationship of /people/person/profession with /m/01d_h8', '/m/07nznf has a relationship of /film/actor/film./film/performance/film with /m/01qb5d', '/m/07nznf has a relationship of /film/producer/film with /m/044g_k', '/m/07nznf has a relationship of /tv/tv_producer/programs_produced./tv/tv_producer_term/producer_type with /m/0ckd1', '/m/07nznf has a relationship of /film/producer/film with /m/016fyc', '/m/07nznf has a relationship of /people/person/profession with /m/03gjzk', '/m/07nznf has a relationship of /people/person/ethnicity with /m/041rx', '/m/07nznf has a relationship of /film/producer/film with /m/02qhlwd', '/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/044g_k', '/m/07nznf has a relationship of /film/director/film with /m/044g_k', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award with /m/040njc', '/m/07nznf has a relationship of /base/popstra/celebrity/friendship./base/popstra/friendship/participant with /m/015v3r', '/m/07nznf has a relationship of /film/producer/film with /m/0cd2vh9', '/m/07nznf has a relationship of /film/director/film with /m/0d90m', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award with /m/0fbtbt', '/m/07nznf has a relationship of /film/director/film with /m/01qb5d', '/m/07nznf has a relationship of /film/director/film with /m/016fyc', '/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/0d90m', '/m/07nznf has a relationship of /people/person/education./education/education/institution with /m/01hb1t', '/m/07nznf has a relationship of /people/person/profession with /m/02jknp', '/m/07nznf has a relationship of /people/person/place_of_birth with /m/02_286', '/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/0cd2vh9', '/m/07nznf has a relationship of /tv/tv_producer/programs_produced./tv/tv_producer_term/program with /m/04p5cr', '/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/award with /m/02g3ft', '/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/honored_for with /m/0d90m', '/m/07nznf has a relationship of /people/person/gender with /m/05zppz', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award_nominee with /m/0h53p1', '/m/07nznf has a relationship of /base/popstra/celebrity/friendship./base/popstra/friendship/participant with /m/01k53x', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award_nominee with /m/013pk3', '/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/honored_for with /m/044g_k', '/m/07nznf has a relationship of /people/person/profession with /m/02hrh1q']"

    str = ent_str.split(";")

    # str = ta.clean(str)
    entity_symbol = str[0]
    entity_name = ta.clean(str[1])
    entity_des = ta.clean(str[2])
    # print(str[2])

    # print(ta.clean(ast.literal_eval(str[3])[0]))

    li = ast.literal_eval(str[3])
    print("neighbours : ",len(li))

    entity_description_list = []

    entity_description_list.append(entity_symbol)

    entity_description_list += entity_name

    entity_description_list += entity_des

    neighbours_li = []

    for i in range(len(li)):

        re_list = li[i].split(" ") # 分解每个邻居
        # print(re_list)
        sub_re_list = re_list[1:-1]
        # print(sub_re_list)
        w_list = [re_list[0]] # 取头实体
        for j in range(len(sub_re_list)):
            w_list += ta.clean(sub_re_list[j])

        w_list.append(re_list[-1]) # 取尾巴实体
        print(i)
        print(w_list)
        entity_description_list += w_list
        neighbours_li.append(w_list)

    # print(neighbours_li)
    print("neighbours : ", len(neighbours_li))

    print(entity_description_list)
    print(len(entity_description_list))

    # print(eval(str[3])[0])


    # 做一个词库，包含所有实体和关系

def read_word_bag(in_path):
    """
    read training data (complex_triple2vector)
    :param in_path:
    :param all_data:  return data
    :return:
    """
    print("read world bag \n")
    all_data = []
    all_word = {}

    try:
        fopen_in = open(in_path,  'r')
    except IOError as err:
        print('file open error: {0}'.format(err))
    else:
        i = 0
        for eachLine in fopen_in:
            if eachLine:
                each = eachLine.strip()
                all_data.append(each)
                all_word[each] = i
                i += 1

        fopen_in.close()

    print("read train data over! ")
    # all_word_bag = all_data
    return all_data,all_word

def load_w2v_vec(fname, vocab):
    """
    Loads 300x1 word vecs from Google (Mikolov) word2vec
    """
    print("load bin vec \n")

    word_vecs = {}
    with open(fname, "rb") as f:
        header = f.readline()
        vocab_size, layer1_size = map(int, header.split())
        binary_len = np.dtype('float32').itemsize * layer1_size
        c = 0
        for line in range(vocab_size):
            word = []
            while True:
                ch = f.read(1).decode('latin-1')
                if ch == ' ':
                    word = ''.join(word)
                    break
                if ch != '\n':
                    word.append(ch)

            if word in vocab:
               word_vecs[word] = np.fromstring(f.read(binary_len), dtype='float32')
               c +=1
            else:

                f.read(binary_len)
    return word_vecs

def load_golve_vec(word_list):

    print("load bin vec \n")

    word_vectors = {}
    c = 0
    for w in glove.itos:
        if w in word_list:
            word_vectors[w] = glove[w]
            c += 1

    print(len(word_list), c, len(word_list) - c)

    return word_vectors

def word2vector(word_dict):
    """

    """
    print("World to vector ... \n")
    # word2vector
    word_to_idx = word_dict #数据集中所有的单词
    print(word_to_idx)
    print(len(word_to_idx))

    pretrained_embeddings = np.random.uniform(-0.25, 0.25, (len(word_dict), 300))

    # word2vec = load_w2v_vec('./data/GoogleNews-vectors-negative300.bin', word_to_idx)
    word2vec = load_golve_vec(word_to_idx)

    for word, vector in word2vec.items(): # 初始化每个词

        pretrained_embeddings[word_to_idx[word]] = vector


    print("NULL -> ",word_to_idx['NULL'],pretrained_embeddings[0])

    # print("contemporary -> ",pretrained_embeddings[30080])
    # print("/m/01cvxf - > ",pretrained_embeddings[0])


import random
# 生成指定范围内不重复的随机整数
# a_int = int(input("请输入随机整数范围起始值："))
# b_int = int(input("请输入随机整数范围结束值："))
# c_int = int(input("请输入随机数个数："))


def int_random(a, b, n) :
    # 定义一个空列表存储随机数
    a_list = []
    while len(a_list) < n :
        d_int = random.randint(a, b)
        if(d_int not in a_list) :
            a_list.append(d_int)
        else :
            pass
    # 将生成的随机数列表转换成元组并返回
    return a_list






if __name__=="__main__":

    """
    Obtain entity2id and relation2id. (25 Mar)
    """
    # entity2id_path = "./FB15K/entity2id.txt"
    # data_id = read_ent_rel_2id(entity2id_path)
    #
    # print(data_id[:,0].tolist())

    # relation2id_path = "./FB15K/relation2id.txt"
    # data_id = read_ent_rel_2id(relation2id_path)
    #
    # print(data_id[0,0])
    #
    # train_id_path = "./FB15K/train2id.txt"
    # train2id = train_id = read_data2id(train_id_path)
    # print(train2id[0,:])

    # text clearn
    # entity_text_process()
    # relation_text_process()
    # neighbours = ['the entity has not neighbours']
    # print(neighbours)
    # print(type(neighbours))

    """word2vector"""
    # word_bag_path = "FB15K/word_bag.txt"
    # wb_list,all_word_dic = read_word_bag(word_bag_path)
    # word2vector(all_word_dic)

    # print(wb_list)
    # print(len(wb_list))

    print(int_random(0, 10, 3))

    a = np.random.uniform(-0.25, 0.25, 50)
    print(type(a))
