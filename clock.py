from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('This job is run every ten seconds.')
    call_command('resetruta')
    print('complete.')

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every minute.')
    call_command('resetruta')
    print('complete.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
