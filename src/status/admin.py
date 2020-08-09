from django.contrib import admin

from .models import Status
from .forms import Statusform


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form = Statusform
    # class Meta:
    #     model = Status

admin.site.register(Status,StatusAdmin)