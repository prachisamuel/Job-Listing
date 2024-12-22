from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        extra_kwargs = {
            'employment_type': {'required': False},
            'posted_date': {'required': False},
            'description': {'required': False},
            'details_url': {'required': False},
        }
