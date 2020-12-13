from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Recommend, Plant

# Register your models here.
class PlantAdmin(ImportExportModelAdmin):
    model=Plant
    list_display=('symbol','scientific_name','common_name','duration','growth_habit')

admin.site.register(Recommend)
admin.site.register(Plant,PlantAdmin)