from django.db import models

# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=40)
    age= models.IntegerField()
    email= models.EmailField()
    place= models.CharField(max_length=30)

    # def __str__(self):
    #     self.name