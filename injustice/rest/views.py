from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest.serializers import *
from rest.renderers import *
from rest.filters import *
from rest.converters import *
from twilio import twiml
from twilio.rest import TwilioRestClient
from django_twilio.decorators import twilio_view
import django_twilio.request as dt

@twilio_view
def received_message(request):
    client = TwilioRestClient()
    twilio_request = dt.decompose(request)

    from_ = twilio_request.from_

    client.sms.messages.create(to=from_, from_="+14155992671", body="Gotcha message, d-boi!") 

class CourtByAddress(generics.ListCreateAPIView):
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = CourtSerializer

    def get(self, request, *args, **kwargs):
        address = str(self.kwargs['address'])

        if address is not None:
            coords = address_to_coords(address)
            lat = coords['lat']
            lng = coords['lng']

            court = get_court_id(lat, lng)

            if court != {}:
                response = Response(court, status=status.HTTP_200_OK)
                if response is not None: 
                    return response 

class CourtByLocation(generics.ListCreateAPIView):
    """
    API endpoint that returns a court for a set of coordinates
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
