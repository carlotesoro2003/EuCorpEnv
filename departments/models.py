from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DepartmentHeads(models.Model):
    head = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, blank=True, null=True, default='')
    is_admin = models.BooleanField(default=False)  # Field to identify admin user

    def __str__(self):
        return f"{self.department.name}"
