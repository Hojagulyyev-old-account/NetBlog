from django.db import models

# Create your models here.
class Code(models.Model):
	code = models.CharField('Junior code', max_length=30)

	def __str__(self):
		return self.code
