import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_other_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently'

	def __str__(self):
		'''
		Адекватно выводилась инфа в консоль
		:return: str
		'''
		return self.question_text


class Choise(models.Model):
	question = models.ForeignKey(Question)
	choise_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		'''
		Адекватно выводилась инфа в консоль
		:return: str
		'''
		return self.choise_text

