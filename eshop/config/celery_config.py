import os
from celery import Celery
from kombu import Exchange, Queue


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

basedir = os.getcwd()
task_folder = os.path.join(basedir, 'notifications', 'app_tasks')

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith('tasks_') and filename.endswith('.py'):
            module_name = f"notifications.app_tasks.{filename[:-3]}"
            module = __import__(module_name, fromlist=['*'])

            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith('task_'):
                    task_modules.append(f'{module_name}.{name}')

    app.autodiscover_tasks(task_modules)