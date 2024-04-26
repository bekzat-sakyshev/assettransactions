from django.contrib import admin
from .models import Asset, Transaction

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['asset', 'transaction_date', 'quantity', 'amount']