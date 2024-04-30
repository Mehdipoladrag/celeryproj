import os
from celery import Celery, Task
from kombu import Exchange, Queue
import logging

class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("Connection Error Occurred in project. Custom Task Handeler")
        else :
            print(f'task id: {task_id} got error ')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.Task = CustomTask
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter', routing_key='dead_letter')
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

app.autodiscover_tasks()
