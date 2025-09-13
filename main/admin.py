from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'engine_cc', 'kilometers', 'price', 'location')
    search_fields = ('brand', 'model', 'location')
    list_filter = ('year', 'fuel_type', 'owner_type')

