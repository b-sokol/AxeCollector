from django.db import models
from django.urls import reverse
from datetime import date
from dateutil.relativedelta import relativedelta, MO
from sortedm2m.fields import SortedManyToManyField

SERVICES = (
  ('R', 'Restring'),
  ('S', 'Setup'),
  ('E', 'Electronics'),
  ('C', 'Structural Repair'),
  ('F', 'Fretwork'),
)

class String(models.Model):
  brand = models.CharField(max_length=50)
  line = models.CharField(max_length=50)
  material = models.CharField(max_length=50, blank=True)
  guage = models.CharField(max_length=50)
  @property
  def name(self):
    return "%s %s" % ( self.brand, self.line )
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('strings_detail', kwargs={'pk': self.id})

class Axe(models.Model):
  name = models.CharField(max_length=100)
  year = models.IntegerField()
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  serial_number = models.CharField(max_length=100, blank=True)
  description = models.TextField(max_length=250)
  setup_specs = models.TextField(max_length=250, blank=True)
  strings = SortedManyToManyField(String, blank=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'axe_id': self.id})

  def needs_service(self):
    return self.maintenance_set.count() == 0 or self.maintenance_set.first().date.__str__() <= (date.today()+relativedelta(months=-1)).__str__()

class Maintenance(models.Model):
  date = models.DateField('maintenance date')
  service = models.CharField(
    max_length=1,
    choices=SERVICES,
    default=SERVICES[0][0]
    )
  technician = models.CharField(max_length=50, default='Me')
  axe = models.ForeignKey(Axe, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_service_display()} on {self.date}'
  
  class Meta:
    ordering = ['-date']