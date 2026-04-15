from django.db import models


class ShipmentStatus(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=150)
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    status = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"
