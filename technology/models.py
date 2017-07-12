from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Part(models.Model):
	"""docstring for part"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'القسم'
		verbose_name_plural = 'الأقسام'

class Blog(models.Model):
	"""docstring for Blog"""
	title = models.CharField(max_length=200,verbose_name='العنوان')
	date = models.DateTimeField('تاريخ النشر')
	publisher = models.ForeignKey(User)
	body = models.TextField()
	image = models.ImageField()
	views = models.IntegerField(default=0)
	part = models.ForeignKey(Part)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'التدوينة'
		verbose_name_plural = 'التدوينات'


class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	birth = models.DateField()
	photo = models.ImageField()
	nabda = models.CharField(max_length=300)
	class Meta:
		verbose_name = 'الصفحة الشخصية'
		verbose_name_plural = 'الصفحات الشخصية'