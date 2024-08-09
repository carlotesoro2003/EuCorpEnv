from django.db import models
from departments.models import DepartmentHeads
from django.utils.timezone import now

# Create your models here.
class Opportunities(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    head = models.ForeignKey(to=DepartmentHeads, on_delete=models.CASCADE)
    statement = models.TextField(default='')
    plannedActions = models.TextField(default='')
    kpi = models.TextField(default='')
    keyPersons = models.TextField(default='')
    targetOutput = models.TextField(default='')
    budget = models.FloatField()
    startDate = models.DateField(default=now)
    endDate = models.DateField(default=now)