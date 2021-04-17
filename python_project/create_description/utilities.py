
import os
import numpy as np
import pandas as pd
import ast
from text_analytics.text_analytics.text_analytics import text_analytics
ta = text_analytics()

class Enti(object):
    def __init__(self, _id, _symbal, _label, _description, _neighbours, _entity2vec,_entity_des_word_list = None):
        self.id = str(_id)

        self.symb = _symbal
        self.label = _label
        self.description = _description
        self.neighbours = _neighbours
        self.entity2vec = _entity2vec
        self.entity_des = _entity_des_word_list

    def print_enti(self):
        print("id: ", self.id, '\n'
                               "symbal: ", self.symb,
              "label: ", self.label,
              "description: ", self.description)

    def get_random_neighbour(self):
        """
        randomly return a neighbours
        """
        num_neighbours = len(self.neighbours)

        if num_neighbours == 0:
            res = "the entity has not neighbours"
        else:
            index = np.random.random_integers(0, num_neighbours - 1)  # readomly select a neighbour
            res = str(self.neighbours[index])

        return res

    def get_des(self):

        des = str(self.symb) + '$' + str(self.label) + '$' + str(self.description) + '$' + str(self.neighbours)

        return des

    def set_entity_des(self,_entity_des):
        self.entity_des = _entity_des

    def get_entity_description(self):
        return self.entity_des




class Rela(object):
    def __init__(self, _id, _name, _mention, _neighbours, _rel2vec,_rel_des_word_list = None):

        self.id = str(_id)

        self.name = _name
        self.mention = _mention
        self.neighbours = _neighbours
        self.rel2vec = _rel2vec
        self.relation_des = _rel_des_word_list

    def set_relation_description(self,_relation_des):
        self.relation_des = _relation_des

    def get_relation_description(self):
        return self.relation_des


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



def relation_text_process(rel_str_list):
    """
    given a relation , which was transformed into a word vector
    """
    # rel_str = "/film/actor/film./film/performance/film, which is between /m/07nznf and /m/014lc_;/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/award with /m/02g3ft;/m/014lc_ has a relationship of /film/film/release_date_s./film/film_regional_release_date/film_release_region with /m/0f8l9c"
    relation_des_word_list = []

    for rel_str in rel_str_list:

        rel_str = rel_str.split(";")
        relation_mention = rel_str[0]
        relation_neighbours = rel_str[1:]

        relation_mention_list = relation_mention.split(" ")
        # print(relation_mention_list)
        relation_mention = ta.clean(relation_mention_list[0])

        relation_mention += relation_mention_list[1:]

        relation_description_list = []
        relation_description_list += relation_mention
        neighbours_li = []
        #
        for i in range(len(relation_neighbours)):

            re_list = relation_neighbours[i].split(" ") # 分解每个邻居

            sub_re_list = re_list[1:-1]

            w_list = [re_list[0]] # 取头实体

            for j in range(len(sub_re_list)):
                w_list += ta.clean(sub_re_list[j])

            w_list.append(re_list[-1]) # 取尾巴实体

            relation_description_list += w_list

            neighbours_li.append(w_list)

        relation_des_word_list.append(relation_description_list)

    return relation_des_word_list



def entity_text_process(ent_str):
    """
    given a entity , which was transformed into a word vector
    """

    # ent_str = "/m/07nznf;Bryan Singer;American film director, writer and producer;" \
    #       "['/m/07nznf has a relationship of /people/person/nationality with /m/09c7w0', " \
    #       "'/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/nominated_for with /m/04p5cr', " \
    #       "'/m/07nznf has a relationship of /medicine/notable_person_with_medical_condition/condition with /m/029sk', " \
    #       "'/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award_nominee with /m/08xwck', " \
    #       "'/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/nominated_for with /m/016fyc', " \
    #       "'/m/07nznf has a relationship of /film/actor/film./film/performance/film with /m/014lc_', " \
    #       "'/m/07nznf has a relationship of /film/producer/films_executive_produced with /m/01qb5d', " \
    #       "'/m/07nznf has a relationship of /people/person/profession with /m/0dxtg', " \
    #       "'/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/01qb5d', " \
    #       "'/m/07nznf has a relationship of /base/schemastaging/person_extra/net_worth./measurement_unit/dated_money_value/currency with /m/09nqf', " \
    #       "'/m/07nznf has a relationship of /film/director/film with /m/02qhlwd', " \
    #       "'/m/07nznf has a relationship of /people/person/education./education/education/institution with /m/065y4w7', '/m/07nznf has a relationship of /people/person/profession with /m/01d_h8', '/m/07nznf has a relationship of /film/actor/film./film/performance/film with /m/01qb5d', '/m/07nznf has a relationship of /film/producer/film with /m/044g_k', '/m/07nznf has a relationship of /tv/tv_producer/programs_produced./tv/tv_producer_term/producer_type with /m/0ckd1', '/m/07nznf has a relationship of /film/producer/film with /m/016fyc', '/m/07nznf has a relationship of /people/person/profession with /m/03gjzk', '/m/07nznf has a relationship of /people/person/ethnicity with /m/041rx', '/m/07nznf has a relationship of /film/producer/film with /m/02qhlwd', '/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/044g_k', '/m/07nznf has a relationship of /film/director/film with /m/044g_k', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award with /m/040njc', '/m/07nznf has a relationship of /base/popstra/celebrity/friendship./base/popstra/friendship/participant with /m/015v3r', '/m/07nznf has a relationship of /film/producer/film with /m/0cd2vh9', '/m/07nznf has a relationship of /film/director/film with /m/0d90m', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award with /m/0fbtbt', '/m/07nznf has a relationship of /film/director/film with /m/01qb5d', '/m/07nznf has a relationship of /film/director/film with /m/016fyc', '/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/0d90m', '/m/07nznf has a relationship of /people/person/education./education/education/institution with /m/01hb1t', '/m/07nznf has a relationship of /people/person/profession with /m/02jknp', '/m/07nznf has a relationship of /people/person/place_of_birth with /m/02_286', '/m/07nznf has a relationship of /film/film_story_contributor/film_story_credits with /m/0cd2vh9', '/m/07nznf has a relationship of /tv/tv_producer/programs_produced./tv/tv_producer_term/program with /m/04p5cr', '/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/award with /m/02g3ft', '/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/honored_for with /m/0d90m', '/m/07nznf has a relationship of /people/person/gender with /m/05zppz', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award_nominee with /m/0h53p1', '/m/07nznf has a relationship of /base/popstra/celebrity/friendship./base/popstra/friendship/participant with /m/01k53x', '/m/07nznf has a relationship of /award/award_nominee/award_nominations./award/award_nomination/award_nominee with /m/013pk3', '/m/07nznf has a relationship of /award/award_winner/awards_won./award/award_honor/honored_for with /m/044g_k', '/m/07nznf has a relationship of /people/person/profession with /m/02hrh1q']"

    str = ent_str.split("$")

    # str = ta.clean(str)
    entity_symbol = str[0]
    entity_name = ta.clean(str[1])
    entity_des = ta.clean(str[2])
    # print(str[2])

    # print(ta.clean(ast.literal_eval(str[3])[0]))
    # print("=====errs=====")
    # print(str)

    li = ast.literal_eval(str[3])

    # print("neighbours : ",len(li))

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
        # print(i)
        # print(w_list)
        entity_description_list += w_list
        neighbours_li.append(w_list)

    # print(neighbours_li)
    # print("neighbours : ", len(neighbours_li))

    # print(entity_description_list)
    # print(len(entity_description_list))

    return entity_description_list

    # print(eval(str[3])[0])


    # 做一个词库，包含所有实体和关系
