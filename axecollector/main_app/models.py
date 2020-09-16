from django.db import models

# Create your models here.
class Axe(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name