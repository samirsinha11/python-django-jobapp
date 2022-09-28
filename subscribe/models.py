from django.db import models
NEWSLETTER = [('M', 'Monthly'), ('W','Weekly')]
# Create your models here.
class Subscribe(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    newsletter =models.CharField(max_length=2, choices=NEWSLETTER, default='M')