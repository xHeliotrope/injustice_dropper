from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest.serializers import *

class CitationByLocation(generics.ListCreateAPIView):
    """
    API endpoint that list citations by coordinates
    """
    serializer_class = CitationViolationSerializer

    def get_queryset(self):
        


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
