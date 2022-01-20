from django.db import models


class Contact_en(models.Model):
	subject = models.CharField('Subject', max_length=50)
	email = models.EmailField('E-mail', max_length=50)
	message = models.TextField('Message', max_length=1500)

	def __str__(self):
		return self.email
