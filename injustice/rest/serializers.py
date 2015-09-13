from rest_framework import serializers
from rest.models import *

class CourtSerializer(serializers.Serializer):
    class Meta:
        resource_name = 'courts'

class CitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citations
        resource_name = 'citations'

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violations
        resource_name = 'violations'

class WarrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrants
        resource_name = 'warrants'

class CitationViolationSerializer(serializers.ModelSerializer):
    violations = ViolationSerializer(many=True, read_only=True)

    class Meta:
        model = Citations
        resource_name = 'citations'
        fields = ('citation_date', 'first_name', 'last_name', 'date_of_birth', 'defendant_address', 'defendant_city', 'defendant_state', 'drivers_license_number', 'court_date', 'court_location', 'court_address', 'violations')
