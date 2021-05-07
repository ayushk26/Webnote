from django.db import models

# Create your models here.

class Note(models.Model):
    username = models.TextField(max_length=30)
    title = models.TextField(max_length=50)
    description = models.TextField(max_length= 150)
    active = models.BooleanField(default=True)

