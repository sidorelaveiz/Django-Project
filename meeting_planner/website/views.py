from django.shortcuts import render, get_object_or_404, redirect
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


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "website/detail.html",
                  {"meeting": meeting})

def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    if request.method == "POST":
        meeting.tittle = request.POST['tittle']
        meeting.date = request.POST['date']
        meeting.start_time = request.POST['start_time']
        meeting.duration = request.POST['duration']
        meeting.save()
        return redirect('welcome')

    return render(request, "website/edit.html", {"meeting": meeting})
