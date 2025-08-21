from django.db import models

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

# Now we need to tell it to create the table by applying a migration
