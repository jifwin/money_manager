from django.db import models

# Create your models here.

class Entry(models.Model):
	#todo: use python month from library
	month = models.CharField(max_length=200)
	amount = models.IntegerField(default=0)
