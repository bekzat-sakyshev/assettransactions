from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Asset(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    asset_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    asset_object_id = models.PositiveIntegerField()
    asset = GenericForeignKey('asset_content_type', 'asset_object_id')
    transaction_date = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset} - {self.transaction_date}"
