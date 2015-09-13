from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest.serializers import *
from rest.renderers import *
from rest.filters import *

class CourtByLocation(generics.ListCreateAPIView):
    """
    API endpoing that returns a court for a set of coordinates
    """
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = CourtSerializer

    def get(self, request, *args, **kwargs):
        lat = float(self.kwargs['lat'])
        lng = float(self.kwargs['lng'])

        if lat is not None and lng is not None:
            court = get_court_id(lat, lng)

            if court != {}:
                response = Response(court, status=status.HTTP_200_OK)
                return response

class CitationByLocation(generics.ListCreateAPIView):
    """
    API endpoint that list citations by coordinates
    """
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = CitationViolationSerializer

    def get_queryset(self):
        lat = float(self.kwargs['lat'])
        lng = float(self.kwargs['lng'])

        if lat is not None and lng is not None:
            court_name = get_court_id(lat, lng)

            if court_name != {}:
                print(next(iter(court_name.keys())))
                return Citations.objects.all().filter(court_location__icontains=next(iter(court_name.keys())))

        return queryset.none()

class CitationList(generics.ListCreateAPIView):
    """
    API endpoint that lists citations (for testing only)
    """
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = CitationSerializer

    def get_queryset(self):
        return Citations.objects.all()

class ViolationList(generics.ListCreateAPIView):
    """
    API endpoint that lists citations (for testing only)
    """
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = ViolationSerializer

    def get_queryset(self):
        return Violations.objects.all()

class CitationViolationList(generics.ListCreateAPIView):
    """
    API endpoint that lists citations and accompanying
    violations (for testing only)
    """
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = CitationViolationSerializer

    def get_queryset(self):
        return Citations.objects.all()
