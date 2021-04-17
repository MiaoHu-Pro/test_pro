#! /usr/bin/python3
#-*-coding:utf-8-*-
import sys


import numpy as np
import pandas as pd
import time
import os

"""
读取 train， test ， valid 文件，获取全部triples，写入 all_triples
"""

def read_file(in_path,all_data):
    'used to read a text file.'

    num = 0
    try:
        fopen_in = open(in_path,  'r')

    except IOError as err:
        print('file open error: {0}'.format(err))
    else:
        for eachLine in fopen_in:
            #print(eachLine)
            num +=1

            all_data.append(eachLine)

        fopen_in.close()
        print(num)




def write_to_file(out_path,all_data):

    ls = os.linesep

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:

        fobj.writelines(['%s' % x for x in all_data])

        fobj.close()

    print('WRITE FILE DONE!')





if  __name__=='__main__':

    train_file = "./FB15K-237/train.txt"
    test_file = "./FB15K-237/test.txt"
    valid_file = "./FB15K-237/valid.txt"

    out_data_file = "./FB15K-237/all_triples.txt"


    list_path = [train_file,test_file,valid_file]
    all_data = []
    #
    for file in list_path:

        read_file(file,all_data)
        print("num_triple : ", len(all_data))
        time.sleep(2)


    all_data = list(set(all_data))
    print("去重复之后，num_triple : ", len(all_data))
    write_to_file(out_data_file,all_data)







