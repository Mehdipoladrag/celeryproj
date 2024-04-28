from celery import shared_task

@shared_task(queue='tasks')
def send_sms():
    print("SMS has been successfully sent")
