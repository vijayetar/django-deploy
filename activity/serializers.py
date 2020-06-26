from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    fields=('event_name','event_duration','event_date', 'event_user')
    model = Event