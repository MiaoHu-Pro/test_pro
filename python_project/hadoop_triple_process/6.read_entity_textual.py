import numpy as np

import pandas as pd

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

    # entity_des = read_files("./dataset_v2/all_issues_textual/entity_textual_info.txt")
    # print(entity_des.shape)

    """
    Ticket-no	        HADOOP-18367
    id	                28    
    Summary	            S3A prefetching to update IOStatisticsContext
    Project	            HADOOP
    IssueType	        Improvement
    Status	            Open
    Sub-task	        []
    IssuelinksCount	    2      
    Issuelinks	        [<JIRA IssueLink: id='12644477'>, <JIRA IssueLink: id='12644478'>]
    Created time	    2022-07-26T11:07:55.000+0000
    Updated time	    2022-07-26T11:09:51.000+0000
    attachment	        []
    resolution	        None
    priority            Major
        
    """

    entity_des2 = pd.read_csv("dataset_v2/all_issues_textual/entity_textual_info3.txt", sep="\t")
    entity_des2 = np.array(entity_des2)
    print(entity_des2[:,7].tolist())
    print(sum(entity_des2[:,7]))
    print(entity_des2.shape)

    print(entity_des2[1:30,9].tolist())
    # print(entity_des2[1:30,10].tolist())


