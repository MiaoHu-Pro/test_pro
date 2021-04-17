#! /usr/bin/python3
#-*-coding:utf-8-*-
import sys


import json
import time
from KGObject import Enti
def read_json(path):
    entity_list = list()
    with open(path, 'r') as f:

        data = json.load(f)# 读取json
    #
    #
    for key,value in data.items():
        pass

       # print('{key}:{value}'.format(key = key, value = value))
        #print(key)
    # print(data, type(data))
    entity_list = list(data.items()) # 将dict_items转换成列表

    return entity_list
    #print(type(ims)) # <class 'dict_items'>
    #

def define_entityObj(entity_list):


    num = len(entity_list)
    enti_Ob_list = list()

    for i in range(num):
        """
        print(
            "id:",i,
            "symbal:", entity_list[i][0],
              "lable:",dict(entity_list[i][1])['label'],
              "description:",dict(entity_list[i][1])['description']) #  第一实体的符号，和lable  
        """

        #封装对象

        enti = Enti(_id= i,
                    _symbal=entity_list[i][0],
                    _lable=dict(entity_list[i][1])['label'],
                    _description=dict(entity_list[i][1])['description'])
        enti_Ob_list.append(enti)

    return enti_Ob_list

def wirte_file(enti_Ob_list,out_path):

    num = len(enti_Ob_list)
    print(num)
    Header = "id " + "\t"+ " symbal" + "\t  "+  "   lable" + "\t     "+ "description" + '\n'



    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:

        fobj.writelines(Header)


        fobj.writelines(['%s \t %s \t %s\t %s \n'% (x.id, x.symb, x.lable, x.description) for x in enti_Ob_list])

        fobj.close()


def obtain_entity_obj():

    path = './FB15K/entity2wikidata.json'

    all_entity  = read_json(path)

    enti_Ob_list = define_entityObj(all_entity)

    return enti_Ob_list

if  __name__=='__main__':


    w_path = 'FB15K237/entity2Obj.txt'
    path = './FB15K-237/entity2wikidata.json'
    all_entity  = read_json(path)
    print(len(all_entity))
    enti_Ob_list = define_entityObj(all_entity)
    # 写文件
    wirte_file(enti_Ob_list,w_path)
    print("END\n")
