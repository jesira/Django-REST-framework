from django.db import models


class Employee(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)


class Owner(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    owner_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
