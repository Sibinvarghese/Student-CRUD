from django.db import models
from phone_field import PhoneField

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Student(models.Model):
    fname=models.CharField(max_length=120)
    lname=models.CharField(max_length=120)
    phnumber=PhoneField(blank=True,help_text='Contact phone number')
    age=models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

