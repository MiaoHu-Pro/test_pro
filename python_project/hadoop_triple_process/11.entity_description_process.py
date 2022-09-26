

import os
import re
import time

import cytoolz as ct
import numpy as np
import pandas as pd
from gensim.parsing import preprocessing


def clean(line):
    function_words_1 = ["the", "of", "and", "to", "a", "in", "i", "he", "that", "was", "it", "his", "you", "with", "as",
                        "for", "had", "is", "her", "not", "but", "at", "on", "she", "be", "have", "by", "which", "him",
                        "they", "this", "from", "all", "were", "my", "we", "one", "so", "said", "me", "there", "or",
                        "an", "are", "no", "would", "their", "if", "been", "when", "do", "who", "what", "them", "will",
                        "out", "up", "then", "more", "could", "into", "man", "now", "some", "your", "very", "did",
                        "has", "about", "time", "can", "little", "than", "only", "upon", "its", "any", "other", "see",
                        "our", "before", "two", "know", "over", "after", "down", "made", "should", "these", "must",
                        "such", "much", "us", "old", "how", "come", "here", "never", "may", "first", "where", "go", "s",
                        "came", "men", "way", "back", "himself", "own", "again", "say", "day", "long", "even", "too",
                        "think", "might", "most", "through", "those", "am", "just", "make", "while", "went", "away",
                        "still", "every", "without", "many", "being", "take", "last", "shall", "yet", "though",
                        "nothing", "get", "once", "under", "same", "off", "another", "let", "tell", "why", "left",
                        "ever", "saw", "look", "seemed", "against", "always", "going", "few", "got", "something",
                        "between", "sir", "thing", "also", "because", "yes", "each", "oh", "quite", "both", "almost",
                        "soon", "however", "having", "t", "whom", "does", "among", "perhaps", "until", "began",
                        "rather", "herself", "next", "since", "anything", "myself", "nor", "indeed", "whose", "thus",
                        "along", "others", "till", "near", "certain", "behind", "during", "alone", "already", "above",
                        "often", "really", "within", "used", "use", "itself", "whether", "around", "second", "across",
                        "either", "towards", "became", "therefore", "able", "sometimes", "later", "else", "seems",
                        "ten", "thousand", "don", "certainly", "ought", "beyond", "toward", "nearly", "although",
                        "past", "seem", "mr", "mrs", "dr", "thou", "except", "none", "probably", "neither", "saying",
                        "ago", "ye", "yourself", "getting", "below", "quickly", "beside", "besides", "especially",
                        "thy", "thee", "d", "unless", "three", "four", "five", "six", "seven", "eight", "nine",
                        "hundred", "million", "billion", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
                        "ninth", "tenth", "amp", "m", "re", "u", "via", "ve", "ll", "th", "lol", "pm", "things", "w",
                        "didn", "doing", "doesn", "r", "gt", "n", "st", "lot", "y", "im", "k", "isn", "ur", "hey",
                        "yeah", "using", "vs", "dont", "ok", "v", "goes", "gone", "lmao", "happen", "wasn", "gotta",
                        "nd", "okay", "aren", "wouldn", "couldn", "cannot", "omg", "non", "inside", "iv", "de",
                        "anymore", "happening", "including", "shouldn", "yours", ]
    function_words_2 = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
                        'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
                        'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
                        'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                        'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
                        'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
                        'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
                        'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                        'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
                        'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                        'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm',
                        'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn',
                        'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
    function_words = function_words_2 + function_words_1
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

    line = [x for x in line if x not in function_words]

    return line

def write_ID_Name_Mention(out_path,data):

    ls = os.linesep
    num = len(data)

    try:
        fobj = open(out_path,  'w')
    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        for j in range(num):
            #
            _str = str(j) + '\t' + data[j][0] + '\t' + data[j][1] + '\t' + data[j][2] + '\n'

            fobj.writelines('%s' % _str)

        fobj.close()

    print('WRITE FILE DONE!')

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
    description
    Created time	    2022-07-26T11:07:55.000+0000
    Updated time	    2022-07-26T11:09:51.000+0000
    attachment	        []
    resolution	        None
    priority            Major
        
    """

    entity_des2 = pd.read_csv("./hadoop_with_other_components/HBASE_textual_info.txt", sep="\t")
    entity_des2 = np.array(entity_des2)

    # lc = entity_des2[:,7]
    # print("lc: ", sum(lc))
    time.sleep(1)

    # id_list = entity_des2[:,0].tolist()
    # name_list = entity_des2[:,2].tolist()
    # mention_list = entity_des2[:,9].tolist()
    row,colum = entity_des2.shape

    id_name_mention = []
    for i in range(row):
        print(i)
        _id_name_mention = []
        Id = entity_des2[i][0]

        Name = clean(entity_des2[i][2])
        Name = ' '.join(Name)
        Mention = clean(entity_des2[i, 9])
        Mention = ' '.join(Mention)

        if len(Name) == 0:
            Name = "None"

        if len(Mention) == 0:
            Mention = "None"

        _id_name_mention.append(Id)
        _id_name_mention.append(Name)
        _id_name_mention.append(Mention)

        id_name_mention.append(_id_name_mention)
        # print("id_name_mention",id_name_mention)


    print("len(id_name_mention)",len(id_name_mention))
    write_ID_Name_Mention("./hadoop_with_other_components/HBASE_ID_Name_Mention.txt", id_name_mention)

    # for i in range(len(des_list)):
    #     print(i)
    #     print(des_list[i])
    #     _des = clean(des_list[i])
    #
    #     print(_des,'\n')
    #     time.sleep(1)


"""
{code} ... {code}

['aws', 'sdk', 'update', 'address', 'jackson', 'cve'] == > 
'aws sdk update address jackson cve',  

"""