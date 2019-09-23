from django.shortcuts import render
from rest_framework import viewsets
from .models import operational_parameter
from .serializer import Op_Serializer

# Create your views here.
class OpViewset(viewsets.ModelViewSet):
    queryset = operational_parameter.objects.all()
    serializer_class = Op_Serializer
