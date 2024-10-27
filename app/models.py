from django.db import models
from django.utils import timezone

class Catchment(models.Model):
    name = models.CharField(max_length=30,unique=True)

class Project(models.Model):
    name = models.CharField(max_length=100,unique=True,default=timezone.now)
    catchment = models.ForeignKey(Catchment, on_delete=models.CASCADE,related_name="project")
    project_code = models.CharField(max_length=50, default="None", null=True, blank=True)
    Phase_Name = models.CharField(max_length=30, default="undefined", null=True, blank=True)
    target_HHs = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    enrolled_HHs = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    project_id = models.CharField(max_length=30,default="undefined", null=True, blank=True)

    

#	catchment_name								form_number	full_name			Phone Number	

class Person(models.Model):
    first_name = models.CharField(max_length=30,default="undefined")
    last_name = models.CharField(max_length=30,default="undefined")
    full_name = models.CharField(max_length=60)
    form_number = models.CharField(max_length=30,primary_key=True)
    phoneNumber = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    national_id = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    gender = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    district_name = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    traditional_authority_name = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    group_village_head_name = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    village_name = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    household_id = models.CharField(max_length=30,default="undefined", null=True, blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="person")   										

class Forms(models.Model):
    formNumber = models.CharField(max_length=30,unique=True)
    phoneNumber = models.CharField(max_length=30, null=True,blank=True)