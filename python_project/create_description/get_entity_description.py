
# 获取ID + Description + neighbor 结构，并进行world嵌入

import numpy as np
import pandas as pd
import os
from utilities import entity_text_process
from text_analytics.text_analytics.text_analytics import text_analytics
import torch
import torchtext
import re
from get_word2vector import word2vector
from utilities import Enti

ta = text_analytics()
glove = torchtext.vocab.GloVe(name="6B", dim=300)
r_glove = torchtext.vocab.GloVe(name="6B", dim=300)

def read_file(in_path):
    """
    read training data (complex_triple2vector)
    :param in_path:
    :param all_data:  return data
    :return:
    """
    all_data = []

    try:
        fopen_in = open(in_path,  'r')
    except IOError as err:
        print('file open error: {0}'.format(err))
    else:
        for eachLine in fopen_in:
            if eachLine:
                each = eachLine.split(',')
                elements = []
                for n in each:
                    n = re.sub(r'[\[\]]', '', n)
                    elements.append(float(n))

                all_data.append(elements)
        fopen_in.close()

    print("read train data over! ")
    return pd.DataFrame(all_data)

def read_all_data(path):

    f = open(path)
    x = []
    relation_set = []
    entity_set = []
    entityPair_set = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split('\t')

            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements

            x.append(d)
            relation_set.append(d[1])
            entity_set.append(d[0])
            entity_set.append(d[2])
            entityPair_set.append((d[0],d[2]))

    f.close()
    X = np.array(x)

    return X , relation_set,entity_set,set(entityPair_set)

def read_train_set(path):

    f = open(path)
    x = []
    relation_set = []
    h_entity_set = []
    t_entity_set = []
    entityPair_set = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split('\t')

            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements

            x.append(d)
            relation_set.append(d[1])
            h_entity_set.append(d[0])
            t_entity_set.append(d[2])
            entityPair_set.append((d[0],d[2]))

    f.close()
    X = np.array(x)
    return X, relation_set, h_entity_set,t_entity_set ,entityPair_set
def read_entity2id(data_id_paht):

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
    data_id = np.array(data_id)
    return data_id

def read_entity_obj(entity_obj_path):

    """
    14344(index) 	/m/0wsr(symbol) 	 Atlanta Falcons(label)	 American football team (description)
    :param entity_obj_path:
    :return:
    """
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

def set_entity_obj(X,sub_x_obj,_entity_set):

    """
    :param X: triples
    :param sub_x_obj: there are 14515 entities have label and des.
    :param entity_set: there are 14951 entities
    :return: 14951 entity objects
    """

    entity_symbol_set = _entity_set

    num_entity = len(entity_symbol_set)
    all_head = list(X[:,0]) # 取出所有的头实体，然后获取其邻居
    all_entity_obj_list = []
    all_entity_description_list = []

    new_word_bag = ['NULL']
    new_word_bag += ['has', 'a', 'relationship', 'of','with','which','is','between','and']
    max_neighbours = 0
    for i in range(num_entity):

        print(i)
        entity_symbol = entity_symbol_set[i]
        # print(entity_symbol)
        # 获取每一个实体的邻居
        entity_index_list = [i for i, x in enumerate(all_head) if x == entity_symbol] # Count neighbors

        # 封装邻居属性
        entity_neighbours = X[entity_index_list,1:3].tolist()

        if len(entity_neighbours) > max_neighbours:
            max_neighbours = len(entity_neighbours)

        # print(entity_neighbours)
        # 封装其他属性
        sybmol = list(sub_x_obj[:,1])

        entity_id = i

        if entity_symbol in sybmol:
            index = sybmol.index(entity_symbol)
            # print(sub_x_obj[index,:])
            entity_label = sub_x_obj[index,2]
            entity_des = sub_x_obj[index,3]

        else:
            entity_label = "The entity has not label"
            entity_des = "The entity has not description "

        """
         /m/01xpxv has a relation of /people/person/ethnicity with /m/0cn68.
         
         str1 = " has a relation of "
         
         str2 =  " with "
         
         neighbour = entity_symbol + str1 +  entity_neighbours[i][0] + str2 + entity_neighbours[i][1]
         
        """

        str1 = " has a relationship of "
        str2 = " with "
        entity_neighbours_list = []
        str_entity_neighbours = []

        if len(entity_neighbours) == 0:
            str_entity_neighbours = ['this entity has not neighbours']
        elif len(entity_neighbours) > 0 and len(entity_neighbours) < 20:
            for i in range(len(entity_neighbours)):

                neighbour = entity_symbol + str1 + entity_neighbours[i][0] + str2 + entity_neighbours[i][1]
                str_entity_neighbours.append(str(neighbour))
        else:
            for i in range(20):

                neighbour = entity_symbol + str1 + entity_neighbours[i][0] + str2 + entity_neighbours[i][1]
                str_entity_neighbours.append(str(neighbour))

            # entity_neighbours_list.append(neighbour)
        # print(str_entity_neighbours)

        # print(str_entity_neighbours)

        # 随机生成结构信息
        entity_id2vec = np.random.rand(100)
        # 封装完整实体
        """"
        此时可以进行实体描述的词列表封装
        des = str(self.symb) + '$' + str(self.label) + '$' + str(self.description) + '$' + str(self.neighbours)
        
        """

        en_des = str(entity_symbol) + '$' + str(entity_label) + '$' + str(entity_des) + '$' + str(str_entity_neighbours)
        entity_des_word_list = entity_text_process(en_des) # get entity des 's word list

        entity = Enti(_id=entity_id, _symbal=entity_symbol, _label=entity_label,_description=entity_des, _neighbours=str_entity_neighbours,
                      _entity2vec=entity_id2vec,_entity_des_word_list=entity_des_word_list)

        all_entity_obj_list.append(entity)

        # 用list记录所有实体的描述，
        en_des_word_list = entity.get_entity_description()
        all_entity_description_list.append(en_des_word_list)

        # 记录词表
        new_word_bag += entity_des_word_list
        new_word_bag = list(set(new_word_bag))
        # entity_obj.append(Enti(_id=entity_id,_symbal=entity_symbol,_label=entity_label,_description=entity_des, _neighbours=str_entity_neighbours,_entity2vec= entity_id2vec))

    print("set_entity_description_obj --> Over ! ")
    print(new_word_bag,len(new_word_bag))

    word_bag_dic = {}
    for i in range(len(new_word_bag)):
        word_bag_dic[new_word_bag[i]] = i
    write_to_file("FB15K/new_word_bag.txt", new_word_bag)
    print(word_bag_dic)

    pre_word_embedding = word2vector(word_bag_dic)

    print("max_neighbours:\n",max_neighbours)


    return all_entity_obj_list,all_entity_description_list, new_word_bag,word_bag_dic,pre_word_embedding

def write_train_set():
    pass


def write_triples2vector(_triple2vector):

    out_path = "./FB15K/all_complex_triple2vector.txt"
    fobj = open(out_path,  'a+')

    fobj.writelines('%s\n' % _triple2vector)

    fobj.close()

def write_to_file(out_path,all_data):

    ls = os.linesep

    try:
        fobj = open(out_path,  'w')
    except IOError as err:

        print('file open error: {0}'.format(err))

    else:

        fobj.writelines('%s\n' % x for x in all_data)

        fobj.close()

    print('WRITE FILE DONE!')

def write_to_file_entity_obj(out_path,all_data):

    ls = os.linesep

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        for x in all_data:

            # _str = str(x.id) + '\t' + str(x.symb) + '\t' + str(x.label) + '\t' + str(x.description)+ '\t' + str(x.neighbours) + '\t' + str(x.entity2vec) + '\n'
            #
            _str = str(x.id) + '\t' + str(x.symb) + '\t' + str(x.label) + '\t' + str(x.description)+ '\t' + str(x.neighbours) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')

def write_entity2vec(out_path,all_data,entity_set):

    ls = os.linesep

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        for x in all_data:

            _str = str(x.id) + '\t' + str(x.symb) + '\t' + str(x.entity2vec) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')

def stop_w2embedd(str):
    _str = str
    s_list = ta.clean(_str)
    em_list = []
    for c in s_list:
        _c = list(glove[c])
        em_list.append(_c)
    em_arr = np.array(em_list)
    _vec = np.mean(em_arr,axis=0)
    return _vec

def relation_stop_w2embedd(str):
    _str = str
    s_list = ta.clean(_str)
    em_list = []
    for c in s_list:
        _c = list(r_glove[c])
        em_list.append(_c)
    em_arr = np.array(em_list)
    _vec = np.mean(em_arr,axis=0)
    return _vec


def creat_nes_con_features(X, entity_set, set_entity_obj,out_path):
    """

    :param X: training data
    :param entity_set: entity set
    :param set_entity_obj: entity obj set
    :return: [[[h_syb,h_label,h_des,h_neighbour],[r_word: h has a relation of r with h1],[t_syb,t_label,t_des,t_neighbour]],
                [],...,]
    """

    '''
    text pre-processing
    1、stop word
    2、glove
    '''
    # out_path = "./FB15K/all_complex_triple2vector.txt"
    fobj = open(out_path,  'a+')

    fix_c = ' has a relation of with '

    fix_c_vec = stop_w2embedd(fix_c)

    #构造每一个实体描述（id + symbol + label + des + neighb）

    # triples_set = [] # contain 3 elements h , r and t
    # triples2vector = []

    for i in range(len(X)):# we will get each triple.

        print(i)
        # _triples_set = []
        _triples2vector = []

        h_neighbour2vec = []
        t_neighbour2vec = []

        h_list = []
        r = []
        t_list = []

        h_list_2vec = []
        t_list_2vec = []

        h = X[i][0]
        t = X[i][2]

        r.append(X[i][1])

        '''
        
        relation2vec
        r_id randomly generate
        r_des /./././. + which is between h.lab ant t.lab 
        
        '''
        # -===========================================
        #
        # relation = X[i][1]
        # r_2vec = relation_stop_w2embedd(str(relation))
        #
        # -===========================================

        h_index = entity_set.index(h)
        h_obj = set_entity_obj[h_index]

        t_index = entity_set.index(t)
        t_obj = set_entity_obj[t_index]

        h1 = None
        r1 = None
        #creat sentence as head entity description
        if len(h_obj.neighbours) == 0:

            h_neighbour = " there is no relation "

        else:

            h_num_neighbours = len(h_obj.neighbours)

            index = np.random.random_integers(0,h_num_neighbours - 1) # readomly select a neighbour

            h1 = h_obj.neighbours[index][1]
            r1 = h_obj.neighbours[index][0]

            """
                h_obj.symb -> vec
                " has a relation of " -> vec
                r1  -> vec
                " with"  -> vec
                h1 -> vec
                
            """

            h_neighbour = h_obj.symb + " has a relation of " + r1 + " with " + h1

        # h_list.append(h_obj.symb) # 50
        # h_list.append(h_obj.label) # 50
        # h_list.append(h_obj.description) # 50
        # h_list.append(h_neighbour)# 50

        h_label_vec = stop_w2embedd(str(h_obj.label))
        h_description_vec = stop_w2embedd(str(h_obj.description))

        if r1 is None or h1 is None:
            h_neighbour_r1 = np.random.rand(300)
            h_neighbour_h1 = np.random.rand(300)
        else:

            h_neighbour_r1 = stop_w2embedd(str(r1))

            index_h1 = entity_set.index(h1)
            h1_obj = set_entity_obj[index_h1]
            h_neighbour_h1 = h1_obj.entity2vec

        h_neighbour2vec.append(h_obj.entity2vec)
        h_neighbour2vec.append(fix_c_vec)
        h_neighbour2vec.append(h_neighbour_r1)
        h_neighbour2vec.append(h_neighbour_h1)

        h_neighbour2vec_arr = np.array(h_neighbour2vec)
        h_neighbour2vec_ = np.mean(h_neighbour2vec_arr,axis=0)

        if np.isnan(h_obj.entity2vec).sum() > 0:
            _vec = np.random.rand(300)
            h_obj.entity2vec = _vec.tolist()
            h_list_2vec.append(h_obj.entity2vec)
        else:
            h_list_2vec.append(h_obj.entity2vec)

        if np.isnan(h_label_vec).sum() > 0:
            _vec = np.random.rand(300)
            h_label_vec = _vec.tolist()
            h_list_2vec.append(h_label_vec)
        else:
            h_list_2vec.append(h_label_vec.tolist())

        if np.isnan(h_description_vec).sum() > 0:
            _vec = np.random.rand(300)
            h_description_vec = _vec.tolist()
            h_list_2vec.append(h_description_vec)
        else:
            h_list_2vec.append(h_description_vec.tolist())

        if np.isnan(h_neighbour2vec_).sum() > 0:
            _vec = np.random.rand(300)
            h_neighbour2vec_ = _vec.tolist()
            h_list_2vec.append(h_neighbour2vec_)
        else:
            h_list_2vec.append(h_neighbour2vec_.tolist())


        # print("h_list_2vec ",h_list_2vec)

        # 求均值
        h_list_2vec = np.array(h_list_2vec,dtype=float)
        h_list_2vec = list(np.mean(h_list_2vec,axis=0))

        # print("h_list_2vec", len(h_list_2vec),h_list_2vec)

        # -===========================================

        r1 = None
        t1 = None

        #creat sentence as tail entity description
        if len(t_obj.neighbours) == 0:

            t_neighbour = " there is no relation "

        else:

            t_num_neighbours = len(t_obj.neighbours)

            index = np.random.random_integers(0,t_num_neighbours - 1) # readomly select a neighbour

            t1 = t_obj.neighbours[index][1]
            r1 = t_obj.neighbours[index][0]

            """
                t_obj.symb -> vec
                " has a relation of " -> vec
                r1  -> vec
                " with"  -> vec
                t1 -> vec
                
            """
            t_neighbour = t_obj.symb + " has a relation of " + r1 + " with " + t1

        # t_list.append(t_obj.symb)
        # t_list.append(t_obj.label)
        # t_list.append(t_obj.description)
        # t_list.append(t_neighbour)


        # print("t_obj.symb ",t_obj.symb)
        # print("t_obj.label ",t_obj.label)
        # print("t_obj.description ",t_obj.description)
        # print("t_neighbour ",t_neighbour)

        t_label_vec = stop_w2embedd(str(t_obj.label))
        t_description_vec = stop_w2embedd(str(t_obj.description))

        if r1 is None or t1 is None:

            t_neighbour_r1 = np.random.rand(300)
            t_neighbour_t1 = np.random.rand(300)

        else:
            t_neighbour_r1 = stop_w2embedd(str(r1))
            index_t1 = entity_set.index(t1)  #
            t1_obj = set_entity_obj[index_t1]
            t_neighbour_t1 = t1_obj.entity2vec

        t_neighbour2vec.append(t_obj.entity2vec)
        t_neighbour2vec.append(fix_c_vec)

        t_neighbour2vec.append(t_neighbour_r1)
        t_neighbour2vec.append(t_neighbour_t1)

        t_neighbour2vec_arr = np.array(t_neighbour2vec)
        t_neighbour2vec_ = np.mean(t_neighbour2vec_arr,axis=0)

        if np.isnan(t_obj.entity2vec).sum() > 0:

            _vec = np.random.rand(300)
            t_obj.entity2vec = _vec.tolist()
            t_list_2vec.append(t_obj.entity2vec)
        else:
            t_list_2vec.append(t_obj.entity2vec)

        if np.isnan(t_label_vec).sum() > 0:
            print("t_label_vec is nan")
            _vec = np.random.rand(300)
            t_label_vec = _vec.tolist()
            t_list_2vec.append(t_label_vec)
        else:
             t_list_2vec.append(t_label_vec.tolist())

        if np.isnan(t_description_vec).sum() > 0:
            _vec = np.random.rand(300)
            t_description_vec = _vec.tolist()
            t_list_2vec.append(t_description_vec)
        else:
            t_list_2vec.append(t_description_vec.tolist())

        if np.isnan(t_neighbour2vec_).sum() > 0:
            _vec = np.random.rand(300)
            t_neighbour2vec_ = _vec.tolist()
            t_list_2vec.append(t_neighbour2vec_)
        else:
            t_list_2vec.append(t_neighbour2vec_.tolist())


        # 求均值
        # print("t_list_2vec ",t_list_2vec)

        t_list_2vec = np.array(t_list_2vec,dtype=float)
        t_list_2vec = list(np.mean(t_list_2vec,axis=0))

        # print("t_list_2vec ", len(t_list_2vec),t_list_2vec)

        # -===========================================

        '''
        relation2vec
        r_id randomly generate
        r_des /./././. + which is between h.lab ant t.lab 
        '''
        # -===========================================

        r_des = str(" which is between ") + str(t_obj.label) + str(" and ") + str(h_obj.label)
        relation = X[i][1]
        r_sentence = str(relation) + r_des

        # print("r_sentence: ",r_sentence)

        r_2vec = relation_stop_w2embedd(r_sentence)

        # print("r_2vec ",len(r_2vec),r_2vec)

        # -===========================================

        # _triples_set.append(h_list)
        # _triples_set.append(r)
        # _triples_set.append(t_list)

        _triples2vector.append(h_list_2vec)

        _triples2vector.append(r_2vec.tolist()) # relation embedding

        _triples2vector.append(t_list_2vec)

        # triples_set.append(_triples_set)

        # write to file  write_triples2vector()

        fobj.writelines('%s\n' % _triples2vector)

        # triples2vector.append(_triples2vector)

    fobj.close()
    re = "this fun over"
    return re

if __name__=="__main__":

    """
    生成实体的描述和id向量
    (25 Mar)
    """
    train_path = './FB15K/all_triples.txt'
    set_entity_obj_path = './FB15K/all_entity_description_6.txt'
    entity2vec_path = './FB15K/all_entity2id_randomly_vector_6.txt'

    train_complex_triples_path = './FB15K/all_complex_triples.txt'
    train_complex_triple2vector_path = './FB15K/all_complex_triple2vector.txt'



    # 首先获得entity2Obj，在kg_data_processing 中
    entity_obj_path = './FB15K/entity2Obj.txt'

    X, relation_set, entity_set, entityPair_set = read_all_data(train_path)


    # print("data details")
    # print(X.shape)
    # print(len(relation_set))
    # print(len(entity_set))
    # print("read_train_set ->  over ! ")

    sub_x_obj = read_entity_obj(entity_obj_path) # 14515 entities have label and des , and about 436 has not desc...
    print("read_entity_obj ->  over ! ")

    # print("len(entityPair_set)",len(entityPair_set))

    # print(X.shape)

    relation_set = list(set(relation_set))
    # print("len relation_set",len(relation_set))
    # entity_set = list(set(entity_set))
    # print("len entity_set",len(entity_set))


    # 获取entity id
    entity2id_path = "./FB15K/entity2id.txt"
    entity_id_read_file = read_entity2id(entity2id_path)
    entity_id_set = entity_id_read_file[:,0].tolist()


    """
    set_entity_obj     14951 entities and its description
    all_entity2vec_set 14951 randomly generate vector as entity id
    """

    entity_obj_list, all_entity_description_list, new_word_bag,word_bag_dic,pre_word_embedding = set_entity_obj(X,sub_x_obj,entity_id_set)


    print("set_entity_obj ->  over ! ")
    write_to_file_entity_obj(set_entity_obj_path,entity_obj_list)
    write_entity2vec(entity2vec_path,entity_obj_list,entity_set) #entity_set 与 set_entity_obj对应
    print("write set_entity_obj  ->  over ! ")

    # print('entity_set[1]',entity_set[1])
    # print('set_entity_obj[1].id',set_entity_obj[1].id)
    # print('set_entity_obj[1].symb',set_entity_obj[1].symb)
    # print('set_entity_obj[1].label',set_entity_obj[1].label)
    # print('set_entity_obj[1].description',set_entity_obj[1].description)
    # print('set_entity_obj[1].neighbours',set_entity_obj[1].neighbours)
    # complex_triples_set,triples2vector = creat_nes_con_features(X,entity_set,set_entity_obj)
    # print("creat_nes_con_features ->  over ! ")
    #
    # write_to_file(train_complex_triples_path,complex_triples_set)
    # write_to_file(train_complex_triple2vector_path,triples2vector)
    #
    print("=========OVER==========")














