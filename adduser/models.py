from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    date_created = models.DateField()
