#! /usr/bin/python3
#-*-coding:utf-8-*-
import sys



class Enti(object):
    def __init__(self, _id, _symbal, _lable, _description):

        self.id = str(_id)
        self.symb = _symbal
        self.lable = _lable
        self.description = _description


    def print_enti(self):
        print("id: ", self.id,'\n'
        "symbal: ", self.symb,
        "lable: ", self.lable,
        "description: ", self.description)




class Rel(object):
    def __init__(self):
        pass

class EntiPairObj(object):
    def __init__(self, h_EntiObj, relation_list, t_EntiObj):
        self.H_Enti = h_EntiObj
        self.Relset = relation_list
        self.T_Enti = t_EntiObj
        self.num_relations = len(self.Relset)

    def print_triple(self):
        pass

