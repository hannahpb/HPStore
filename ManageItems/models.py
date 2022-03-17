from django.db import models

# Create your models here.

class hpItems(models.Model):
    hpItem = models.SmallIntegerField(primary_key=True)
    hpName = models.CharField(max_length=50)
    hpDescription = models.TextField(max_length=200)
    hpQty = models.SmallIntegerField
