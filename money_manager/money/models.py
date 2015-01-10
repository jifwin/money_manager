from django.db import models

# Create your models here.

class Entry(models.Model):
	#todo: use python month from library
	#todo: use username django field
	username_id = models.IntegerField(default=0)
	month = models.CharField(max_length=200)
	amount = models.IntegerField(default=0)
