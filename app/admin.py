from django.contrib import admin

# Register your models here.

from .models import OpenCelliD

@admin.register(OpenCelliD)
class OpenCelliDAdmin(admin.ModelAdmin):
    list_display = ('mcc', 'net', 'area', 'cell')
    ordering = ('mcc',)
    search_fields = ('mcc', 'net', 'area', 'cell')

#admin.site.register(OpenCelliD)