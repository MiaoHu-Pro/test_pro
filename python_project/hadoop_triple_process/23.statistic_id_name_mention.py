import numpy as np


def read_entity2obj(entity_obj_path):
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



if __name__ == "__main__":

    idNameMention_path = "./hadoop_data_with_time/ID_Name_Mention.txt"
    idNameMention = read_entity2obj(idNameMention_path)

    row, column = idNameMention.shape

    len_list = []
    for i in range(row):
        _len = len(idNameMention[i][2].split(" "))
        len_list.append(_len)

    print(len_list)
    print(np.mean(len_list))


