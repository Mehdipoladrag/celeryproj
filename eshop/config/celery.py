import os
from celery import Celery
from kombu import Exchange, Queue
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


@app.task(queue='tasks')
def task_1():
    time.sleep(3)
    return


@app.task(queue='tasks')
def task_2():
    time.sleep(3)
    return


@app.task(queue='tasks')
def task_3():
    time.sleep(3)
    return


@app.task(queue='tasks')
def task_4():
    time.sleep(3)
    return


def handle_tasks():
    task_2.apply_async(priority=2)
    task_4.apply_async(priority=4)
    task_1.apply_async(priority=1)
    task_3.apply_async(priority=3)
    task_2.apply_async(priority=2)
    task_4.apply_async(priority=4)
    task_1.apply_async(priority=1)
    task_3.apply_async(priority=3)


# app.conf.task_routes = {
#     'notifications.tasks.send_discount_emails': {'queue': 'queue1'},
#     'notifications.tasks.process_data_for_ml': {'queue': 'queue2'},
# }
# app.conf.task_default_rate_limit = '1/m'
#
# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }


app.autodiscover_tasks()