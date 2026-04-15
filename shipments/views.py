from rest_framework import viewsets
from .models import ShipmentStatus
from .serializers import ShipmentStatusSerializer


class ShipmentStatusViewSet(viewsets.ModelViewSet):
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerializer