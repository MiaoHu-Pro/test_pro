
import os
import re

import numpy as np
import pandas as pd



def read_triple_2id(data_id_paht):
    data = pd.read_csv(data_id_paht)  #
    data = np.array(data)
    data_id = []
    for i in range(len(data)):

        _tmp = data[i][0]
        tmp = _tmp.split(' ')
        if tmp:
            id_list = []
            for s in tmp:
                id_list.append(s.strip())
            data_id.append(id_list)
    data = np.array(data_id)
    return data

def write_relation_to_file(out_path, data):
    ls = os.linesep

    num = len(data)

    try:
        fobj = open(out_path, 'w')
    except IOError as err:

        print('file open error: {0}'.format(err))

    else:

        fobj.writelines('%s\n' % num)

        for j in range(num):
            if j % 5000000 == 0:
                print(j)
            _str = data[j] + "\t" + str(j) + '\n'
            fobj.writelines('%s' % _str)
        fobj.close()

    print('WRITE FILE DONE!')

def write_entity2id_to_file(out_path, data):
    ls = os.linesep

    num = len(data)

    try:
        fobj = open(out_path, 'w')
    except IOError as err:

        print('file open error: {0}'.format(err))

    else:

        fobj.writelines('%s\n' % num)

        for j in range(num):
            if j % 5000000 == 0:
                print(j)
            _str = data[j][0] + '\t' + data[j][1] + '\n'
            fobj.writelines('%s' % _str)
        fobj.close()

    print('WRITE FILE DONE!')

def read_entity2id(data_id_paht):
    data = pd.read_csv(data_id_paht)  #
    data = np.array(data)
    data_id = []
    for i in range(len(data)):

        if i % 500000 == 0:
            print(i)

        _tmp = data[i][0]
        tmp = _tmp.split('\t')
        if tmp:
            id_list = []
            for s in tmp:
                id_list.append(s)
            data_id.append(id_list)
    data_id = np.array(data_id)
    return data_id

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
                id_list.append(s.strip())
            data_id.append(id_list)
    data = np.array(data_id)
    return data

def read_files(rank_path):

    f = open(rank_path)

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

    return np.array(x_obj)

def read_rank(rank_path):

    f = open(rank_path)

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
    return np.array(x_obj)


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(file)
    return L


def write_relation2id_dic(path,data):

    num = len(data)

    try:
        fobj = open(path, 'w')
    except IOError as err:

        print('file open error: {0}'.format(err))

    else:
        fobj.writelines('%s\n' % num)
        for key, value in data.items():
            _str = key + '\t' + value + '\n'
            fobj.writelines('%s' % _str)
        fobj.close()
    print('WRITE FILE DONE!')

def write_dic(path,data):

    file = open(path,'w')
    for key, value in data.items():
        # print(key, value)
        file.write(key + '\t' + str(value) + '\n')

    file.close()


def write_entity_relation_frequency(path,data):
    num = len(data)
    file = open(path, 'w')
    file.writelines('%s\n' % num)
    for e in data:
        file.write(str(e[0]) + '\t' + str(e[1]) + '\n')

    file.close()

def write_triples_2_id(path, data):
    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)

        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\t' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')


def static_frequency(dic_path,data):

    d = data
    # print(d)
    # 创建一个value为0 且键值是从d中获取的字典
    c = dict.fromkeys(d, 0)
    # print(c)
    # 循环d 如果遇到了就在c中+1
    # 有意思的是c中的每个键值一定在d中 所以只要遍历d 然后把value+1就可以了
    for x in d:
        c[x] += 1
    # 这里就统计好了每个值的出现次数
    # print(c)
    # 下面找出次数出现最高的3个数
    from collections import Counter
    c2 = Counter(c)\
    # # 这找出出现次数最高的3个
    print(c2.most_common(3))
    print("how many of c ",len(c))

    sorted_x = sorted(c.items(), key=lambda d: d[1], reverse=True)

    write_entity_relation_frequency(path=dic_path, data= sorted_x)


import os
import re
import cytoolz as ct
from gensim.parsing import preprocessing

def clean(line):

    function_words_single = ["the", "of", "and", "to", "a", "in", "i", "he", "that", "was", "it", "his", "you", "with", "as", "for", "had", "is", "her", "not", "but", "at", "on", "she", "be", "have", "by", "which", "him", "they", "this", "from", "all", "were", "my", "we", "one", "so", "said", "me", "there", "or", "an", "are", "no", "would", "their", "if", "been", "when", "do", "who", "what", "them", "will", "out", "up", "then", "more", "could", "into", "man", "now", "some", "your", "very", "did", "has", "about", "time", "can", "little", "than", "only", "upon", "its", "any", "other", "see", "our", "before", "two", "know", "over", "after", "down", "made", "should", "these", "must", "such", "much", "us", "old", "how", "come", "here", "never", "may", "first", "where", "go", "s", "came", "men", "way", "back", "himself", "own", "again", "say", "day", "long", "even", "too", "think", "might", "most", "through", "those", "am", "just", "make", "while", "went", "away", "still", "every", "without", "many", "being", "take", "last", "shall", "yet", "though", "nothing", "get", "once", "under", "same", "off", "another", "let", "tell", "why", "left", "ever", "saw", "look", "seemed", "against", "always", "going", "few", "got", "something", "between", "sir", "thing", "also", "because", "yes", "each", "oh", "quite", "both", "almost", "soon", "however", "having", "t", "whom", "does", "among", "perhaps", "until", "began", "rather", "herself", "next", "since", "anything", "myself", "nor", "indeed", "whose", "thus", "along", "others", "till", "near", "certain", "behind", "during", "alone", "already", "above", "often", "really", "within", "used", "use", "itself", "whether", "around", "second", "across", "either", "towards", "became", "therefore", "able", "sometimes", "later", "else", "seems", "ten", "thousand", "don", "certainly", "ought", "beyond", "toward", "nearly", "although", "past", "seem", "mr", "mrs", "dr", "thou", "except", "none", "probably", "neither", "saying", "ago", "ye", "yourself", "getting", "below", "quickly", "beside", "besides", "especially", "thy", "thee", "d", "unless", "three", "four", "five", "six", "seven", "eight", "nine", "hundred", "million", "billion", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "amp", "m", "re", "u", "via", "ve", "ll", "th", "lol", "pm", "things", "w", "didn", "doing", "doesn", "r", "gt", "n", "st", "lot", "y", "im", "k", "isn", "ur", "hey", "yeah", "using", "vs", "dont", "ok", "v", "goes", "gone", "lmao", "happen", "wasn", "gotta", "nd", "okay", "aren", "wouldn", "couldn", "cannot", "omg", "non", "inside", "iv", "de", "anymore", "happening", "including", "shouldn", "yours",]
    function_words_single = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

    # Remove links, hashtags, at-mentions, mark-up, and "RT"
    line = re.sub(r"http\S+", "", line)
    line = re.sub(r"@\S+", "", line)
    line = re.sub(r"#\S+", "", line)
    line = re.sub("<[^>]*>", "", line)
    line = line.replace(" RT", "").replace("RT ", "")

    # Remove punctuation and extra spaces
    line = ct.pipe(line,
                   preprocessing.strip_tags,
                   preprocessing.strip_punctuation,
                   preprocessing.strip_numeric,
                   preprocessing.strip_non_alphanum,
                   preprocessing.strip_multiple_whitespaces
                   )

    # Strip and lowercase
    line = line.lower().strip().lstrip().split()

    # line = [x for x in line if x not in function_words_single]

    return line


def write_word_bag(out_path, all_data):
    ls = os.linesep

    try:
        fobj = open(out_path, 'w')
    except IOError as err:

        print('file open error: {0}'.format(err))

    else:

        fobj.writelines('%s\n' % x for x in all_data)

        fobj.close()

    print('WRITE FILE DONE!')
