from django.db import models

class Moshinalar(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/images/")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.CharField(max_length=20)