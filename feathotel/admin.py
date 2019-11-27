from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Enquery

# Register your models here.
class EnqueryAdmin(ModelAdmin):
    list_display=['fname','contactNum','query','query_date']
    list_filter=['query_date']

admin.site.register(Enquery,EnqueryAdmin)
