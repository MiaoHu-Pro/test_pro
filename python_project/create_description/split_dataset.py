import numpy as np
import pandas as pd

from utilities import read_train_valid_test_id
"""
split dataset:
test data: contain new relations
train data : contain all entities and relations 
"""



if __name__ == "__main__":

    train_triples_id = './FB15K237/train2id.txt'
    valid_triples_id = './FB15K237/valid2id.txt'
    test_triples_id = './FB15K237/test2id.txt'

    train_id = read_train_valid_test_id(train_triples_id) # read train id
    valid_id = read_train_valid_test_id(valid_triples_id)
    test_id = read_train_valid_test_id(test_triples_id)

    print(train_id.shape)
    print(valid_id.shape)
    print(test_id.shape)
    # data = X_data[X_data[:,feature_index].argsort()] #按照指定的列排序
    _data_id = np.vstack((train_id,valid_id))
    all_data_id = np.vstack((_data_id,test_id))

    print(all_data_id.shape)

    all_entity = all_data_id[:,0].tolist() + all_data_id[:,1].tolist()
    print("num entity ",len(set(all_entity)))

    all_relation = all_data_id[:,2].tolist()
    print("num relation ",len(set(all_relation)))











