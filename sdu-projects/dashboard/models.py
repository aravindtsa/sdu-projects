from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    begin_date = models.DateField()
    end_date = models.DateField()
    project_for = models.CharField(max_length=200)
    alias_email = models.EmailField()
    status = models.CharField(max_length=200)

class Topology(models.Model):
    name = models.CharField(max_length=200)

class Topology_has_Project_has_Hw(models.Model):
    topology_name = models.ForeignKey(Topology)
    project_name = models.ForeignKey(Project)
    eITMS_no = models.IntegerField()
    hardware_shared = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

class User_has_Project(models.Model):
    user_name = models.ForeignKey(User)
    project_name = models.ForeignKey(Project)
    role = models.CharField(max_length=200)

# Create your models here.
