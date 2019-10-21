from django.db import models

# Create your models here.

class OpenCelliD(models.Model):


	radio = models.CharField(max_length=16,default=0)
	mcc = models.IntegerField(default=0)
	net = models.IntegerField(default=0)
	area = models.IntegerField(default=0)
	cell = models.IntegerField(default=0)
	unit = models.IntegerField(default=0)
	lon = models.FloatField(default=0)
	lat = models.FloatField(default=0)
	range = models.IntegerField(default=0)
	samples = models.IntegerField(default=0)
	changeable = models.IntegerField(default=0)
	created = models.IntegerField(default=0)
	updated = models.IntegerField(default=0)
	averageSignal = models.IntegerField(default=0)