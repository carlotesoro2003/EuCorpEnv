from django.contrib import admin

# Register your models here.
from .models import DepartmentHeads, Department

admin.site.register(DepartmentHeads)
admin.site.register(Department)