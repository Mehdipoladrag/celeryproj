from config.celery_config import app
from celery import group

phone_numbers = [
    '09123456789',
    '09124548754',
    '09037454547',
    '09023575453'
]


@app.task(queue='tasks')
def send_sms_to_user(phone_number: str):
    if phone_number.startswith('0903'):
        raise ValueError('Invalid phone number')

    return f'Message has been sent to {phone_number}'


def handle_result(result):
    if result.successful():
        print(f'Task completed: {result.get()}')
    elif result.failed() and isinstance(result.result, ValueError):
        print(f'Task failed:  {result.result}')
    elif result.status == 'REVOKED':
        print(f'Task was revoked: {result.id}')


def run_tasks():
    task_group = group(send_sms_to_user.s(number) for number in phone_numbers)
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)

    for result in result_group:
        handle_result(result)
