from django.http import HttpResponse
from django.shortcuts import render
from .tasks import *
# Create your views here.


def handle_user_data_sync(request):
    task = send_sms_to_user.apply_async(queue='tasks')
    task.get()
    return HttpResponse("<h1>sync View</h1>")


def handle_user_data_async(request):
    task = send_sms_to_user.apply_async(queue='tasks')
    return HttpResponse("<h1>sync View</h1>")
