from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	desc = models.CharField(max_length=500)
	start_date = models.DateTimeField('Date of Event')
	location = models.CharField(max_length=200)

	def __str__(self):
		return self.title
