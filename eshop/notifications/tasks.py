from celery import shared_task
import logging

@shared_task(queue='tasks')
def my_task():
    try:
        print("This is my task")
        raise ValueError("This is my error")

    except Exception as e:
        logging.error("an exception has been occurred this is text from logging")
        raise ConnectionError("an exception has been occurred")
