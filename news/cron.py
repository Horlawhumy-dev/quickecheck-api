from django_cron import CronJobBase, Schedule
import requests
from .models import HackerNewsID
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5 # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'news.my_cron_job'    # a unique code
    def do(self):

        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)

        result = response.text.split(',')[1:len(response.text.split(','))-2] # in order to trim the last element
        last = response.text.split(',')[-1] # got this from API " 499287535 ] /n" --> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"

        news = 400 # 100 downward/latest
        res = [int(id.strip()) for id in result[news+1:news+6]] # list comprehension

        for id in res:
            news_id = HackerNewsID(hackernews=id)
            news_id.save()

# run to add latest hackernews id to db - python manage.py runcrons 