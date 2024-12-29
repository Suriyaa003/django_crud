from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    age = models.IntegerField(blank=False,null=False)
    gender = models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.name