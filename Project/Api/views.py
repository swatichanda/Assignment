from rest_framework import viewsets
from Api import serializer
from .models import Work

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = serializer
