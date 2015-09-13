from django.shortcuts import render
from django.db.models import Q, CharField
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

class ViolationByCitationNumber(generics.ListCreateAPIView):
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = ViolationSerializer

    def get_queryset(self):
        number = int(self.kwargs['citation_number'])

        return Violations.objects.filter(citation_number=number)

class CitationFuzzy(generics.ListCreateAPIView):
    renderer_classes = (CustomJSONRenderer,)
    serializer_class = CitationViolationSerializer 

    def get_queryset(self):
        term1 = str(self.kwargs['term1'])
        term2 = str(self.kwargs['term2'])

        if term1 is not None and term2 is not None:
            fields = [f for f in Citations._meta.fields if isinstance(f, CharField)]
            term1queries = [Q(**{f.name + '__icontains': term1}) for f in fields]
            term2queries = [Q(**{f.name + '__icontains': term2}) for f in fields]

            qs1 = Q()
            for query in term1queries:
                qs1 = qs1 | query
            qs2 = Q()
            for query in term2queries:
                qs2 = qs2 | query

            return Citations.objects.filter(qs1) & Citations.objects.filter(qs2)

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
