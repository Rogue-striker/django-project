from django.db import models

# Create your models here.
class todolist(models.Model):
    content = models.TextField(max_length= 1000)