from django.shortcuts import render
from rest_framework import generics

from .models import Event
from .serializers import EventSerializer
from .permissions import IsEventUserOrReadOnly

# Create your views here.
class EventList(generics.ListCreateAPIView):
  # permission_classes = (IsEventUserOrReadOnly,)
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsEventUserOrReadOnly,)
  queryset = Event.objects.all()
  serializer_class = EventSerializer
