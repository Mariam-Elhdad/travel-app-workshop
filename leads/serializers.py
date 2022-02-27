from rest_framework import serializers
from home.models import Vehicle 

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vehicle 
    fields = '__all__'