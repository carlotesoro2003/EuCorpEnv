from django.contrib import admin

# Register your models here.
from .models import Position, Lead

admin.site.register(Position)
admin.site.register(Lead)
