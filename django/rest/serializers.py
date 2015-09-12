from rest_framework import serializers
from injustice.models import Citations, Violations

class CitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citations
        resource_name = 'citations'

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violations
        resource_name = 'violations'
