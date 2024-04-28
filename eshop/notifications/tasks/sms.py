from celery import shared_task
from config.celery_config import app



@app.task(queue='tasks', autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
def send_sms():
    raise ConnectionError("Sms Connection Error")

