from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	uid=models.CharField(max_length=50,null=True)
	recipebook=models.IntegerField(default=0)
	signeasy=models.IntegerField(default=0)
	helpchat=models.IntegerField(default=0)
	volt=models.IntegerField(default=0)
	strike=models.IntegerField(default=0)
	buyhatke=models.IntegerField(default=0)
	cleartax=models.IntegerField(default=0)

	def __str__(self):
		return self.name

class total_votes(models.Model):
	recipebook=models.IntegerField(default=0)
	signeasy=models.IntegerField(default=0)
	helpchat=models.IntegerField(default=0)
	volt=models.IntegerField(default=0)
	strike=models.IntegerField(default=0)
	buyhatke=models.IntegerField(default=0)
	cleartax=models.IntegerField(default=0)
