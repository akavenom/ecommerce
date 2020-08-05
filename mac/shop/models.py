from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField # Search Django Field Refrence on Google 
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()