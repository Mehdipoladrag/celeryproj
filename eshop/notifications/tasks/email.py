from celery import shared_task, Task

@shared_task(queue='tasks')
def send_email():
    raise ConnectionError("Connection Error Error Connection")
    print("email has been successfully sent")
