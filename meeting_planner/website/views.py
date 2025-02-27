from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


def date(request):
    return HttpResponse("This oage served at" + str(datetime.now()))


# Create your views here.
def welcome(request):
    meetings = Meeting.objects.all()
    context = {
        'meetings': meetings
    }
    return render(request, 'website/list.html', context)
