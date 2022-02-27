from home.models import Vehicle
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

###Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [ # we need permission classes which is going to be a list and we just want to say permissions , now all is valid
        permissions.IsAuthenticated,
    ]
    # def get_queryset(self):
    #     return self.request.user.leads.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)