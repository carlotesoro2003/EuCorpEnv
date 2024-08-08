from django.db import models, transaction
from departments.models import Department, DepartmentHeads
from leads.models import Lead
from django.utils.timezone import now 

# Create your models here.
class KeyAreas(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(to=DepartmentHeads, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class StrategicGoals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    keyArea = models.ForeignKey(KeyAreas, on_delete=models.CASCADE)
    members = models.ManyToManyField(DepartmentHeads)
    leads = models.ManyToManyField(Lead)  # Ensure this is ManyToManyField if needed
    

    class Meta:
        unique_together = (('goal_id',))

    def save(self, *args, **kwargs):
        if self.pk is None:  # If new object
            # Use a transaction to ensure unique goal_id assignment
            with transaction.atomic():
                existing_ids = set(StrategicGoals.objects.values_list('goal_id', flat=True))
                new_goal_id = 1
                while new_goal_id in existing_ids:
                    new_goal_id += 1
                self.goal_id = new_goal_id
        super(StrategicGoals, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Get the current goal_id
        deleted_id = self.goal_id
        super(StrategicGoals, self).delete(*args, **kwargs)

        # Update subsequent goals' IDs in a transaction
        with transaction.atomic():
            subsequent_goals = StrategicGoals.objects.filter(goal_id__gt=deleted_id)
            for goal in subsequent_goals:
                goal.goal_id -= 1
                goal.save()

    def __str__(self):
        member_names = ', '.join([f"{member.department}" for member in self.members.all()])
        lead_positions = ', '.join([str(lead.position) for lead in self.leads.all()])

        return f"{self.goal_id} - {self.name} - {self.keyArea.name} - Members: {member_names} - Leads: {lead_positions}"


class StrategicObjectives(models.Model):
    objective_id = models.AutoField(primary_key=True)
    goal_id = models.ForeignKey(StrategicGoals, on_delete=models.CASCADE)
    strategicObjectives = models.TextField(default="")
    kpi = models.TextField(default="")
    target = models.TextField(default="")
    evalMeasures = models.TextField(default="")

    def __str__(self):
        kpi_text = self.kpi if self.kpi else "No KPI"
        objectives_text = self.strategicObjectives if self.strategicObjectives else "No Objectives"
        target_text = self.target if self.target else "No Target"
        eval_measures_text = self.evalMeasures if self.evalMeasures else "No Evaluation Measures"
        return f" id : {self.objective_id} | KPI: {kpi_text} | Objectives: {objectives_text} | Target: {target_text} | Evaluation Measures: {eval_measures_text}"
    

class ActionPlans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    objective_id = models.ForeignKey(StrategicObjectives, on_delete=models.CASCADE)
    actionPlan = models.TextField(default='')
    kpi = models.TextField(default='')
    targetOutput = models.TextField(default='')
    personResponsible = models.TextField(default='')
    budget = models.FloatField()
    startDate = models.DateField(default=now)
    endDate = models.DateField(default=now)

    def __str__(self):
        return f"{self.plan_id} - {self.objective_id} - {self.actionPlan}"