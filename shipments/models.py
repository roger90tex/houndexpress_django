from django.db import models
from django.utils import timezone


class Guia(models.Model):
    trackingNumber = models.CharField(max_length=15, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)
    currentStatus = models.CharField(max_length=20)

    class Meta:
        db_table = "Guide"

    def __str__(self):
        return f"{self.trackingNumber} - {self.currentStatus}"


class Estatus(models.Model):
    guideId = models.ForeignKey(Guia, on_delete=models.CASCADE, db_column="guideId")
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
    updatedBy = models.CharField(max_length=20)

    class Meta:
        db_table = "StatusHistory"

    def __str__(self):
        return f"{self.guideId.trackingNumber} - {self.status}"


class Usuario(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.name


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
