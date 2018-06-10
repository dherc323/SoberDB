from django.db import models
from django.urls import reverse
from django.forms import ModelForm, Textarea
# Remember: makemigrations, and then migrate
#Finch class should give a table full of individual bird information.

class Finch(models.Model):
	BirdID = models.CharField(max_length=30, primary_key=True)
	BirdPic = models.FileField(blank = True, default = "No image")
	Location = models.CharField(max_length=30,null = True)
	Origin = models.CharField(max_length=30, null = True)
	Age = models.CharField(max_length=30)
	Parent = models.CharField(max_length=30)
	Procedure = models.CharField(max_length=30)
	Experimenter = models.CharField(max_length=30, blank = True, null=True)
	Spectograms = models.FileField(blank = True, default = "No image")
	Notes = models.TextField(help_text="Add notes here")
	Alive = models.BooleanField()
	Record_Last_Modified = models.DateField(auto_now=True)

	def get_absolute_url(self):
		return reverse('Birds:birdinfo', kwargs={'pk':self.pk})

	def __str__(self):
		return (self.BirdID + "; " +self.Experimenter)

	class Meta:
		verbose_name_plural = "Finch"
