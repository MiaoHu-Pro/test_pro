import numpy as np


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

    total_triples = read_files("./dataset_v3/total_triples.txt")

    not_in_entity_textual_info = read_files("./dataset_v3/not_in_entity_textual_info.txt")


    not_in_entity_textual_info = not_in_entity_textual_info[:,0].tolist()

    print(not_in_entity_textual_info)

    row, colum = total_triples.shape

    total_triples_except_others = []
    removed_triples_from_total = []
    c = 0
    for i in range(row):
        head = total_triples[i][0]
        tail = total_triples[i][2]

        if head not in not_in_entity_textual_info and tail not in not_in_entity_textual_info:
            total_triples_except_others.append(total_triples[i])

        else:
            removed_triples_from_total.append(total_triples[i])
            c += 1

    print("how many triples are remove ",c)


    print("how many triples leave: ", len(total_triples_except_others))

    write_triples("./dataset_v3/new_total_triples.txt",total_triples_except_others)
    write_triples("./dataset_v3/removed_triples_from_total.txt",removed_triples_from_total)

