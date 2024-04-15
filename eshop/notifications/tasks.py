import time
from celery import shared_task


@shared_task
def task_1(rate_limit='1/m'):
    time.sleep(3)
    return


@shared_task
def task_2(queue='celery:1'):
    time.sleep(3)
    return


@shared_task
def task_3(queue='celery:2'):
    time.sleep(3)
    return


@shared_task
def task_4(queue='celery:3'):
    time.sleep(3)
    return


"""
from celery import group, chain
group_tasks = group(task_1.s(),task_2.s(),task_3.s(),task_4.s())
group_tasks.apply_async()
chain_tasks = chain(task_1.s(),task_2.s(), task_3.s(), task_4.s())
chain_tasks.apply_async()
"""
