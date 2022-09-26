import numpy as np
import pandas as pd


def write_triples(path,data):

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

if __name__ == "__main__":

    total_triples_csv = pd.read_csv("./dataset_v3/task1_output2.csv", sep=",",header=None)
    total_triples = np.array(total_triples_csv)

    print(total_triples)

    write_triples("./dataset_v3/total_triples.txt", total_triples)
