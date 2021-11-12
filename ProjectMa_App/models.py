from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Semester(models.Model):
    semester=models.CharField(max_length=10,default='')

    def __str__(self):
        return self.semester

class MCE_CSE_Faculties(models.Model):
    faculty_name=models.CharField(max_length=50,default='')
    project_alloted=models.IntegerField(default=0)
    project_count=models.IntegerField(default=0)
    def __str__(self):
        return self.faculty_name

class MCE_Student_Records(models.Model):
    Semester = models.CharField(max_length=10, default='')
    Mentor_Teacher = models.CharField(max_length=50,default='')
    Group_Name = models.CharField(max_length=20,default='')
    Group_Representative_Name = models.CharField(max_length=50,default='')
    Group_Type = models.CharField(max_length=10,default='')
    Member1_Name = models.CharField(max_length=50,default='')
    Member1_Roll=models.IntegerField(default=False)
    Member2_Name = models.CharField(max_length=50,default='',blank=True)
    Member2_Roll = models.IntegerField(default=0,blank=True)
    Member3_Name = models.CharField(max_length=50,default='',blank=True)
    Member3_Roll = models.IntegerField(default=0,blank=True)
    Member4_Name = models.CharField(max_length=50,default='',blank=True)
    Member4_Roll = models.IntegerField(default=0,blank=True)
    Project_Name = models.CharField(max_length=20, default='')
    Project_Abstract = models.TextField(default='')
    Technologies_to_be_used = models.TextField(default='')
    Project_Report=models.FileField(upload_to="Project_Reports/",default='')
    Project_PPT=models.FileField(upload_to="Project_PPTs/",default='')
    def __str__(self):
        return self.Group_Name

class GroupProfile(models.Model):
    Group_Name= models.CharField(max_length=20,default="")
    Group_Type = models.CharField(max_length=30,default="")
    Group_Representative_Name = models.CharField(max_length=30,default="")

