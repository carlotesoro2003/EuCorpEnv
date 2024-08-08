from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lead(models.Model):
    lastName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.position}"