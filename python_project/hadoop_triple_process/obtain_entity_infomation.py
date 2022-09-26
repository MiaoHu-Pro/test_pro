import re
from jira import JIRA
import warnings
import csv
from datetime import datetime
warnings.filterwarnings('ignore')

list1 = []
with open('./hadoop_with_other_components/not_in_entity_textual_info.txt','r') as f:

    for line in f:
        list1.append(line)

for i in range(len(list1)):
    list1[i]=re.sub('[\n]', '', list1[i])
list1 = list1[1:]


options = {'server': 'https://issues.apache.org/jira', 'verify': False}
# project_str = 'project="HADOOP"'
conn = JIRA(options)
# size  = 100
# initial= 0

with open('./hadoop_with_other_components/not_in_entity_textual_info_part1.csv','w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Ticket-no',
                     'Summary',
                     'Project',
                     'IssueType',
                     'Status',

                     'Sub-task',
                     'IssuelinksCount',
                     'Issuelinks',
                     'Description',

                     'Created time',
                     'Updated time',
                     'attachment',
                     'resolution',
                     'priority'])

s = 0
for i in list1:

    s +=1
    print(s)
    try:
        with open('./hadoop_with_other_components/not_in_entity_textual_info_part1.csv','a+',encoding='utf-8') as f:
            writer = csv.writer(f)

            issue_created_isoformat = (conn.issue(i).fields.created[0:-2] + ':' + conn.issue(i).fields.created[-2:])

            # dt = datetime.fromisoformat(issue_created_isoformat)
            dt = datetime.strptime(issue_created_isoformat, "%Y-%m-%dT%H:%M:%S.%f+00:00")
            writer.writerow([conn.issue(i),
                             conn.issue(i).fields.summary,
                             conn.issue(i).fields.project,
                             conn.issue(i).fields.issuetype.name,
                             conn.issue(i).fields.status.name,

                             conn.issue(i).fields.subtasks,
                             len(conn.issue(i).fields.issuelinks),
                             conn.issue(i).fields.issuelinks,
                             conn.issue(i).fields.description,

                             conn.issue(i).fields.created,
                             conn.issue(i).fields.updated,
                             conn.issue(i).fields.resolution,
                             conn.issue(i).fields.priority])
            f.close()
    except Exception as result:
        print(result)
