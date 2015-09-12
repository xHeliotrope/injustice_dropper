from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest.serializers import *

class FindByLocation(generics.ListAPIView):
    """
    API endpoint which finds data by location in following
    order of precedence: cross street > address > coordinates
    """
    serializer_class = FindByLocationSerializer

    def get_queryset(self):
        # TODO - add lookup logic

class CitationList(generics.ListCreateAPIView):
    """
    API endpoint that lists citations (for testing only)
    """
    serializer_class = CitationSerializer

    def get_queryset(self):
        return Citations.objects.all()

class ViolationList(generics.ListCreateAPIView):
    """
    API endpoint that lists citations (for testing only)
    """
    serializer_class = ViolationSerializer

    def get_queryset(self):
        return Violations.objects.all()
