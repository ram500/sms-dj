from enum import unique
from datetime import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from sqlalchemy import false, null, true
from traitlets import default

# Create your models here.
class Student(models.Model):
 registration_id = models.CharField(max_length=6,primary_key = true, editable = false)
 first_name = models.CharField(max_length=50)
 last_name = models.CharField(max_length=50)
 full_name = models.CharField(max_length=100)
 username = models.CharField(max_length=30)
 date_of_birth = models.DateField()
 date_of_Registration = models.DateField(default=datetime.now().date())
 email = models.EmailField(max_length=100)
 mobile_number = models.CharField(max_length=10)
 gender = models.CharField(max_length=10)
 address = models.CharField(max_length=300)
 city = models.CharField(max_length=30)
 pincode = models.CharField(max_length=10)
 state = models.CharField(max_length=30)
 country = models.CharField(max_length=30)
 class_no = models.IntegerField()
 father_name = models.CharField(max_length=50)
 mother_name = models.CharField(max_length=50)
 password = models.CharField(max_length=30)
 fees = models.BigIntegerField()
 fees_paid = models.BigIntegerField(default=0)
 
 def __str__(self):
  return self.first_name

class Teacher(models.Model):
 registration_id = models.CharField(max_length=6,primary_key = true, editable = false)
 first_name = models.CharField(max_length=50)
 last_name = models.CharField(max_length=50)
 full_name = models.CharField(max_length=100)
 username = models.CharField(max_length=30)
 date_of_birth = models.DateField()
 date_of_Registration = models.DateField(default=datetime.now().date())
 email = models.EmailField(max_length=100)
 mobile_number = models.CharField(max_length=10)
 gender = models.CharField(max_length=10)
 address = models.CharField(max_length=300)
 city = models.CharField(max_length=30)
 pincode = models.CharField(max_length=10)
 state = models.CharField(max_length=30)
 country = models.CharField(max_length=30)
 father_name = models.CharField(max_length=50)
 mother_name = models.CharField(max_length=50)
 password = models.CharField(max_length=30)
 salary = models.BigIntegerField()
 salary_paid = models.BigIntegerField(default=0)  



class Student_attendance(models.Model):
    registration_id = models.CharField(max_length=6,primary_key = true, editable = false)
    date_of_attendance = models.DateField()
    status = models.CharField(max_length=10)