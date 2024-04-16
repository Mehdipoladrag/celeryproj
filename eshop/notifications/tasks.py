import time
from celery import shared_task


@shared_task(queue='tasks')
def send_sms_to_user():
    time.sleep(6)
    print('Sending sms has been successfully sent')