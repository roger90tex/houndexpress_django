from rest_framework import serializers
from .models import ShipmentStatus


class ShipmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentStatus
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']