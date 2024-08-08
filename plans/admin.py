from django.contrib import admin

# Register your models here.
from .models import KeyAreas, StrategicGoals, StrategicObjectives, ActionPlans

admin.site.register(KeyAreas)
admin.site.register(StrategicGoals)
admin.site.register(StrategicObjectives)
admin.site.register(ActionPlans)