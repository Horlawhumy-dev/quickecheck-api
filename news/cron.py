import re
from django_cron import CronJobBase, Schedule
import requests
from .models import News_ID

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'news.my_cron_job'    # a unique code

    def do(self):
        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)
        result = response.text.split(',')[1:len(response.text.split(','))-2] 
        last = response.text.split(',')[-1] # " 499287535 ] /n" -> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"

        news = 10
        # news_to_add = len(response.text.split(',')) - news
        res = [int(id.strip()) for id in result[news+1: news+6]] # list comprehension

        for id in res:
            news_id = News_ID(news=id)
            news_id.save()
        # if len(response.text.split(',')) > (news_to_add + news):
        #     news += news_to_add # this will keep track of differences in length of the data
        # else:
        #     print('No difference in the length')
        print(result)

# run - python manage.py runcrons 