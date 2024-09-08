from django.db import models

# Create your models here.

class Employee(models.Model):

    firstName = models.CharField(max_length=60, blank=True)
    lastName = models.CharField(max_length=60)
    titleName = models.CharField(max_length=60)
    hasPassport = models.BooleanField()
    salary = models.FloatField()
    birthDate = models.DateField()
    hireDate = models.DateField()
    age = models.IntegerField(default=None)
    country = models.CharField(max_length=60, default='')
    dept = models.CharField(max_length=60, default='')
    email = models.EmailField(max_length=100, default=None)
    phoneNumber = models.CharField(max_length=20, default=None)
    def __str__(self):
        return "{} {}".format(self.firstName, self.lastName)
    