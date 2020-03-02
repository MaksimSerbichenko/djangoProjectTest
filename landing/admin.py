from django.contrib import admin
from .models import *


class SabscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sabscriber._meta.fields]
    list_filter = ('name',)
    search_fields = ["name", "email"]

    class Meta:
        model = Sabscriber


admin.site.register(Sabscriber, SabscriberAdmin)
