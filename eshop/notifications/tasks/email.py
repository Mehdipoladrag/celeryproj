from config.celery_config import app
import time

@app.task(queue='tasks', time_limit=5)
def send_email():
    time.sleep(6)
    return "(*Email has been sent to user successfully*)"
