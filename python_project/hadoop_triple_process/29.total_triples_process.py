




import numpy as np
import pandas as pd


def write_triples(path,data):

    try:
        fobj = open(path, 'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        num = len(data)
        print("the number of lines: ",num)
        fobj.writelines('%s\n' % num)
        for k in range(num):
            _str = str(data[k][0]) + '\t' + str(data[k][1]) + '\t' + str(data[k][2]) + '\n'
            fobj.writelines('%s' % _str)

        fobj.close()
    print('WRITE FILE DONE!')

def read_files(rank_path):
    f = open(rank_path)
    f.readline()

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


if __name__ == "__main__":


    total_triples = read_files("./hadoop_with_other_components/YARN_ALL_triplet.txt")



    # total_triples = pd.read_csv("./hadoop_with_other_components/PIG_triplet.csv",header=None)
    # total_triples = np.array(total_triples)


    total_triples = list(total_triples)
    print("len",len(total_triples))

    write_triples("hadoop_with_other_components/YARN_total_triplet.txt", total_triples)


#
