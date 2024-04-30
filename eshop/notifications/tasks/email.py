from config.celery_config import app
import time

@app.task(queue='tasks', time_limit=10)
def send_email():
    time.sleep(6)
    return "(*Email has been sent to user successfully*)"



def send_mail():
    result = send_email.delay()
    try:
        task_result = result.get(timeout=4)

    except TimeoutError:
        print('Task Timed out')
