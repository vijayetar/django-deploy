from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Event(models.Model):
  event_name = models.CharField('Enter Name of Event here: ', max_length=30)
  event_duration = models.IntegerField('Enter duration in minutes: ', default =30)
  event_user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
  event_date = models.DateField('set date here')
  
  def __str__(self):
    return self.event_name
