from rest_framework import serializers
from rest.models import Citations
from rest.models import Violations

class CitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citations
        resource_name = 'citations'

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violations
        resource_name = 'violations'

class CitationViolationSerializer(serializers.ModelSerializer):
    violations = ViolationSerializer(many=True)
    class Meta:
        model = Citations
        resource_name = 'citations'
