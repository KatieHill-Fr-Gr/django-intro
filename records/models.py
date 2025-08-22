from django.db import models

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    label = models.CharField(max_length=255, default='Unsigned')
    sales = models.FloatField(blank=True, null=True)
    album_art = models.URLField(blank=True, null=True)

# Now we need to tell it to create the table by applying a migration
# And every time you update it

