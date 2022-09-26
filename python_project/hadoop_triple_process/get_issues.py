from jira import JIRA
import warnings
import csv
from datetime import datetime
warnings.filterwarnings('ignore')

options = {'server': 'http://issues.apache.org/jira', 'verify': False}
project_str = 'project="HADOOP"'
conn = JIRA(options)
size  = 100
initial= 0

with open('Jira_issues.csv','w',encoding='utf-8') as f:
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
                     'timestamp',
                     'priority'])
        
while True:
    start = initial * size
    issues = conn.search_issues(project_str, startAt=start, maxResults=size)
    if len(issues)==0:
        break
    initial += 1
    with open('Jira_issues.csv','a+',encoding='utf-8') as f:
        writer = csv.writer(f)
        for issue in issues:
            issue_created_isoformat = (issue.fields.created[0:-2] + ':' + issue.fields.created[-2:]).replace('T', ' ')
            dt = datetime.fromisoformat(issue_created_isoformat)
            writer.writerow([issue,
                             issue.fields.summary,
                             issue.fields.project,
                             issue.fields.issuetype.name,
                             issue.fields.status.name,

                             issue.fields.subtasks,
                             len(issue.fields.issuelinks),
                             issue.fields.issuelinks,
                             issue.fields.description,

                             issue.fields.created,
                             issue.fields.updated,
                             issue.fields.attachment,
                             issue.fields.resolution,
                             dt.timestamp(),
                             issue.fields.priority])
