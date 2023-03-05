from django.shortcuts import render
from .models import Record
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import RecordSerializer
# Create your views here.

class RecordListView(ListCreateAPIView):
    queryset=Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Record.objects.all()
    serializer_class = RecordSerializer