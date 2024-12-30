from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from api.models import Lead
from api.serializers import LeadSerializer

class LeadListCreateView(ListAPIView,CreateAPIView):

    queryset=Lead.objects.all()

    serializer_class=LeadSerializer


class LeadRetireveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
     
     queryset=Lead.objects.all()
     
     serializer_class=LeadSerializer


