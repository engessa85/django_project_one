from django.db import models

# Create your models here.

class home_page_model(models.Model):
	first_name = models.CharField(max_length = 30)
	second_name = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 30 , unique = True)
