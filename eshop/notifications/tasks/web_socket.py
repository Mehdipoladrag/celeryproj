from celery import shared_task

@shared_task(queue='tasks')
def send_notif():
    print("notif has been successfully sent")
