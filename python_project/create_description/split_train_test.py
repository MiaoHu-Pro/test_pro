#! /usr/bin/python3
#-*-coding:utf-8-*-

from kg_data_processing_copy.read_json_entity2obj import obtain_entity_obj
import numpy as np
import multiprocessing as mp

from KGObject import EntiPairObj,Enti

# global var
global g_entityPair_set
global g_dataArry
global g_entiObjset
global g_symb_list
global g_h_data
global g_t_data

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

    X = np.array(x)
    return X , relation_set,entity_set,set(entityPair_set)

def entity_pair_rel(g_i):

    entityPair_set = g_entityPair_set
    dataArry = g_dataArry

    entiObjset = g_entiObjset
    symb_list = g_symb_list

    h_data = g_h_data
    t_data = g_t_data

    print(g_i)

    rel_set = []
    head = entityPair_set[g_i][0]
    tail = entityPair_set[g_i][1]

    index_h = [i for i, x in enumerate(h_data) if x == head]
    index_t = [i for i, x in enumerate(t_data) if x == tail]

    com_index = [i for i in index_h if i in index_t]
    # print(com_index)
    for index in com_index:
        rel_set.append(dataArry[index][1])

    # print(head)
    # print(rel_set)
    # print(tail)
    # print("rel_set", rel_set)

    _entityPair_h = None
    _entityPair_t = None

    if head in symb_list:
        _entityPair_h = entiObjset[symb_list.index(head)]
    else:
        _entityPair_h= Enti(_id=None,_symbal=head,_lable=None,_description=None)

    if tail in symb_list:
        _entityPair_t = entiObjset[symb_list.index(tail)]

    else:
        _entityPair_t= Enti(_id=None,_symbal=tail,_lable=None,_description=None)

    pair = EntiPairObj(h_EntiObj=_entityPair_h,relation_list=rel_set, t_EntiObj=_entityPair_t)

    # print("Head lab,symb \n",pair.H_Enti.lable,pair.H_Enti.symb)
    # print("Relations \n",pair.Relset)
    # print("Tail lab \n",pair.T_Enti.lable,pair.T_Enti.symb)
    # print("-------------------------------")
    return pair

def set_entity_pair(dataArry,entityPair_set):

    num_entity_pair = len(entityPair_set)

    global g_entityPair_set
    g_entityPair_set =  entityPair_set

    global g_dataArry
    g_dataArry = dataArry

    global g_h_data
    global g_t_data

    g_h_data = g_dataArry[:, 0]
    g_t_data = g_dataArry[:, 2]

    global g_entiObjset
    g_entiObjset = obtain_entity_obj()

    global g_symb_list
    g_symb_list = list()
    for entiobj in g_entiObjset:
        g_symb_list.append(entiobj.symb)

    Pair_list = []
    pool = mp.Pool(4)
    Pair_list = pool.map(entity_pair_rel,[i for i in range(num_entity_pair)])
    #==========================

    return Pair_list

def split_test_train(pair_set,train_file_path,test_file_path):

    num = len(pair_set)
    print(num)

    try:
        f_train = open(train_file_path,  'w')
        f_test = open(test_file_path,  'w')
        f_all_entityPairs = open('./FB15K/all_entityPairs.txt',  'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:

        for i in range(len(pair_set)):
            X = pair_set[i]

            f_all_entityPairs.writelines(['%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable,X.H_Enti.description, X.Relset[x], X.T_Enti.symb, X.T_Enti.lable,X.T_Enti.description) for x in range(len(X.Relset))])

            if X.num_relations > 1:

                index = np.random.random_integers(0,X.num_relations - 1) #随机移除一个关系，作为测试

                relation_test = X.Relset.pop(index)

                f_train.writelines(['%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable,X.H_Enti.description, X.Relset[x], X.T_Enti.symb,X.T_Enti.lable,X.T_Enti.description) for x in range(len(X.Relset))])

                f_test.writelines('%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable,X.H_Enti.description, relation_test, X.T_Enti.symb,X.T_Enti.lable,X.T_Enti.description))

            else:
                f_train.writelines(['%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb, X.H_Enti.lable,X.H_Enti.description, X.Relset[x], X.T_Enti.symb,X.T_Enti.lable,X.T_Enti.description) for x in range(len(X.Relset))])

        f_train.close()
        f_test.close()
        f_all_entityPairs.close()

def main():

    all_data_file = "./FB15K/all_triples.txt"
    train_file_path = "./FB15K/all_train.txt"
    test_file_path = "./FB15K/all_test.txt"

    print("read all data \n")
    dataArry,relation_set,entity_set,entityPair_set = read_all_data(all_data_file)

    print(dataArry.shape)
    print("numble relation ",len(set(relation_set)))
    print("numble entity ",len(set(entity_set)))
    print("entityPair_set ",len(entityPair_set),len(set(entityPair_set)))

    print("set entity pair，there are relations between entity pairs \n")
    pair_set = set_entity_pair(dataArry,list(entityPair_set))

    print(len(pair_set))

    """
    for i in range(len(pair_set)):
        print("Head  lab \n",pair_set[i].H_Enti.lable)
        print("Relations \n",pair_set[i].Relset)
        print("Tail lab \n",pair_set[i].T_Enti.lable)
    """
    print("split train and test , one of relations to be as test data \n")
    split_test_train(pair_set,train_file_path,test_file_path)

if  __name__=='__main__':

    main()
    print("END !")



