from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class CommonData(models.Model):
    Semester = models.CharField(max_length=10, default='')

    Group_Name = models.CharField(max_length=20,default='')
    Group_Representative_Name = models.CharField(max_length=50,default='')
    Group_Type = models.CharField(max_length=10,default='')
    Member1_Name = models.CharField(max_length=50,default='')
    Member1_Roll=models.IntegerField(default=False)
    Member2_Name = models.CharField(max_length=50,null=True,blank=True)
    Member2_Roll = models.IntegerField(null=True,blank=True)
    Member3_Name = models.CharField(max_length=50,null=True,blank=True)
    Member3_Roll = models.IntegerField(null=True,blank=True)
    Member4_Name = models.CharField(max_length=50,null=True,blank=True)
    Member4_Roll = models.IntegerField(null=True,blank=True)

    class Meta:
        abstract=True

class CommonData2(models.Model):
    Mentor_Teacher = models.CharField(max_length=50, default='')
    Project_Name = models.CharField(max_length=20, default='')
    Project_Abstract = models.TextField(default='')
    Technologies_to_be_used = models.TextField(default='')

    class Meta:
        abstract = True



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


class MCE_Student_Details(CommonData):
    def __str__(self):
        return self.Group_Name

class MCE_Student_Records(CommonData,CommonData2):

    Project_Report = models.FileField(null=True, blank=True, upload_to="Project_Reports/")
    Project_PPT = models.FileField(null=True, blank=True, upload_to="Project_PPTs/")

    def __str__(self):
        return self.Group_Name

class GroupProfile(models.Model):
    Group_Name= models.CharField(max_length=20,default="")
    Group_Type = models.CharField(max_length=30,default="")
    Group_Representative_Name = models.CharField(max_length=30,default="")

class ReportDetails(CommonData2):

    Group_Name = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.Group_Name




