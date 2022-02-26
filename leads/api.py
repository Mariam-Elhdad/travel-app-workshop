from home.models import Vehicle
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [ 
        permissions.AllowAny, #the premision now is valid to all of us 
    ]
    serializer_class = LeadSerializer