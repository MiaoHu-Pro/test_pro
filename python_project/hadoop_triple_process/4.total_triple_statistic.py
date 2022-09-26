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


def write_entity_relation_frequency(path, data):
    num = len(data)
    file = open(path, 'w')
    file.writelines('%s\n' % num)
    i = 0
    for e in data:
        file.write(str(i) + '\t' + str(e[0]) + '\t' + str(e[1]) + '\n')
        i += 1

    file.close()


def static_frequency(dic_path, data):
    d = data
    c = dict.fromkeys(d, 0)
    for x in d:
        c[x] += 1
    sorted_x = sorted(c.items(), key=lambda d: d[1], reverse=True)

    write_entity_relation_frequency(path=dic_path, data=sorted_x)


if __name__ == "__main__":
    total_triples = read_files("dataset_v3/new_total_triples.txt")

    relation_list = total_triples[:, 1].tolist()

    static_frequency("dataset_v3/relation_frequency.txt", relation_list)

    entity_list = total_triples[:, 0].tolist() + total_triples[:, 2].tolist()

    static_frequency("dataset_v3/entity_frequency.txt", entity_list)
