from django.db import models
from datetime import date
from django.utils import timezone

class JobModel(models.IntegerChoices):
	SRE = 1, 'Site Reliability Engineer'
	DEV = 2, 'Developer'
	MAN = 3, 'Manager'
	DIR = 4, 'Director'

class UserModel(models.Model):
	name: str = models.CharField(max_length=100, null=False, blank=False)
	age: int = models.IntegerField(null=False, blank=False)
	job: JobModel = models.IntegerField(choices=JobModel.choices, null=False, blank=False)
	activate: bool = models.BooleanField(default=False, blank=False)
	created_at: timezone.now = models.DateField(null=False, blank=False, default=timezone.now)
	updated_at: timezone.now = models.DateField(null=False, blank=False, default=timezone.now)

	def __str__(self):
		return f'{self.id} - {self.name} - {self.job}'
