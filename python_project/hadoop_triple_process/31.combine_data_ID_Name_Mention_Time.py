import numpy as np


def read_ID_Name_Mention_Time(entity_obj_path):

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

def write_ID_Name_Mention_Time(out_path,data):

    num = len(data)

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        for j in range(num):
            #
            _str = str(j) + '\t' + data[j][1] + '\t' + data[j][2] + '\t' + data[j][3] + '\t' + data[j][4] + '\n'

            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')


if __name__ == "__main__":

    files_name = ['hadoop_common_ID_Name_Mention_Time.txt','HBASE_ID_Name_Mention_Time.txt','HDFS_ID_Name_Mention_Time.txt',
                  'HDT_ID_Name_Mention_Time.txt','HIVE_ID_Name_Mention_Time.txt','MAPREDUCE_ID_Name_Mention_Time.txt','PIG_ID_Name_Mention_Time.txt',
                  'YARN_ID_Name_Mention_Time.txt','not_in_entity_textual_info_part1_ID_Name_Mention_Time.txt']
    #
    # files_name = ['total_entity_ID_Name_Mention_Time.txt','not_in_entity_textual_info_part1_ID_Name_Mention_Time.txt']

    total_entity2obj = []
    for file_name in files_name:
        print("file name:", file_name)

        _entity2obj = read_ID_Name_Mention_Time("./hadoop_with_other_components/" + file_name).tolist()

        total_entity2obj += _entity2obj

    print("len(total_entity2obj)", len(total_entity2obj))


    total_entity_dic = {}
    for i in range(len(total_entity2obj)):

        total_entity_dic[total_entity2obj[i][1]] = i

    print("move repeat entity, how many entity : ", len(total_entity_dic))

    total_entity2obj_after_remove_repeat = []

    # total_entity2obj = np.array(total_entity2obj)

    for key,value in total_entity_dic.items():
        print(key)
        total_entity2obj_after_remove_repeat.append(total_entity2obj[value])

    print("move repeat entity, how many is entity2obj ", len(total_entity2obj_after_remove_repeat))

    write_ID_Name_Mention_Time("hadoop_with_other_components/total_entity_ID_Name_Mention_Time_adv.txt", total_entity2obj_after_remove_repeat)
