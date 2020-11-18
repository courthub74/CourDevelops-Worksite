from django.db import models

# Create your models here.

class Projects(models.Model):
	projects = models.CharField(max_length=200)
	projectscomplete = models.BooleanField(default=False)

	def __str__(self):
		return self.projects 


class Deliverables(models.Model):
	delivs = models.CharField(max_length=200)
	delivscomplete = models.BooleanField(default=False)

	def __str__(self):
		return self.delivs


class Practices(models.Model):
	practices = models.CharField(max_length=200)
	practicescomplete = models.BooleanField(default=False)

	def __str__(self):
		return self.practices


class Classes(models.Model):
	classes = models.CharField(max_length=200)
	classescomplete = models.BooleanField(default=False)

	def __str__(self):
		return self.classes 