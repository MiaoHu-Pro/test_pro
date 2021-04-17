


def read_data(in_path):
    'used to read a text file.'

    relation_set = []
    num = 0
    try:
        fopen_in = open(in_path,  'r')

    except IOError as err:
        print('file open error: {0}'.format(err))
    else:
        for eachLine in fopen_in:

            relation_set.append(eachLine.strip())

            num +=1

        fopen_in.close()

    print(num)
    return relation_set


def num_triples_verification(path_train,path_test):

    num_train = 0
    num_test = 0

    num_train = read_data(path_train)

    num_test = read_data(path_test)

    print("num_train : ",num_train)
    print("num_test : ",num_test)


    return num_train + num_test

def read_write_my_relation_data(input_path,out_relation_path):

    # 手写读取数据
    f = open(input_path,'r')
    relation_x = []

    for d in f:
        d = d.strip()
        if d:
            d = d.split('\t')
            # 每个元素转为int
            relation_x.append(d[0].strip())


    relation_x = list(set(relation_x))
    print("num_relation \n",len(relation_x))

    try:
        fobj = open(out_relation_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:

        fobj.writelines(['%s \n' % x for x in relation_x])

        fobj.close()

def relation_verification(my_relation_path,article_relation_path,):

    my_relation_set = read_data(my_relation_path)
    a_relation_set = read_data(article_relation_path)

    """以a、b、c为实验对象，求 a 中有，但 b 和 c 都没有的元素的并集"""

    r = list(set(my_relation_set).difference(a_relation_set))# 求特定1个list(a)中有，其他list(b、c)都没有的元素"""
    print('r -->', r)   # 输出：r --> [1, 3, 4]"""


"""
/m/02cqbx       /award/award_winner/awards_won./award/aware_honor/honored_for   /m/072192
in all dataset , there is relation ,/award/award_winner/awards_won./award/aware_honor/honored_for ,between Edith Head(/m/02cqbx)  and   A Place in the Sun(/m/072192)	

bgiut the relation does not in the relation2id.

cat ./FB15K/all_triples.txt | grep /award/award_winner/awards_won./award/aware_honor/honored_for
/m/02cqbx       /award/award_winner/awards_won./award/aware_honor/honored_for   /m/072192

"""

if __name__ == "__main__":

    # print("start!")
    # path_train = './FB15K/all_train.txt'
    # path_test = './FB15K/all_test.txt'
    # print("train data and test verification \n")
    # num_all_triples = num_triples_verification(path_train,path_test)
    # print("all triples :",num_all_triples)
    #
    #
    # article_relation = './FB15K/all_train.txt'
    # path_test = './FB15K/all_test.txt'
    # print("relation verification,  1346 or 1345\n")
    # num_all_triples = num_triples_verification(path_train,path_test)
    #
    #
    # read_write_my_relation_data('./FB15K/relation2id.txt','./FB15K/relation_set.txt')
    #
    #

    relation_verification('./FB15K/my_code_relation_set.txt','./FB15K/relation_set.txt')





    print("END!")

