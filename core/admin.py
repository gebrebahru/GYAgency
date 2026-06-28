from django.contrib import admin
from .models import Asset, Worker

admin.site.register(Asset)
admin.site.register(Worker)