from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.DEBUG)  # INFO

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

sched = BlockingScheduler()
import os

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    can = os.environ.get('TEST_CLOCK')
    if ( can == '1' ):
        print('This job is run every minute.')
        os.system("python manage.py resetruta")
        print('Clear ruta.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=23)
def scheduled_job():
    print('This job is run every weekday at 11pm.')
    os.system("python manage.py resetruta")
    print('Clear ruta.')

sched.start()
