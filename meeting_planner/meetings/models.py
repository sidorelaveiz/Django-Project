from django.db import models
from datetime import time



class Room(models.Model):
    name= models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()



class Meeting(models.Model):
    tittle = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default = time(9))
    duration = models.IntegerField(default = 1)

    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
# Create your models here.