from django.db import models
from django.core.urlresolvers import reverse

# Model to track individual Projects and some information about them
class Project(models.Model):
    name = models.CharField( max_length = 50, unique = True, )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField( max_length = 50, )
    information = models.CharField( max_length = 300, )

    def __unicode__(self):
        return self.name

# Model to track individual hardware and it's information, including what Project 
#  the hardware is a part of
class Hardware(models.Model):
    eITMS_code = models.CharField( max_length = 7, unique = True, )
    project = models.ForeignKey('Project')
    manufacturer = models.CharField( max_length = 100, )
    model_code = models.CharField( max_length = 100, )
    lab = models.CharField( max_length = 100, )
    aisle = models.CharField( max_length = 100, blank = True, )
    location_in_aisle = models.CharField( max_length = 100, blank = True, )
    financial_owner = models.IntegerField()
    status = models.CharField( max_length = 100, )
    serial_number = models.CharField( max_length = 50, unique = True)
    parent_serial_number = models.ForeignKey('self', to_field='serial_number', blank = True, null = True, )
    project_name = models.CharField( max_length = 100, )
    comment = models.CharField( max_length = 140, blank = True, )

    def __unicode__(self):
        return 'eITMS: %s - Model: %s - S/N: %s - Project: %s' % (self.eITMS_code, self.model_code, self.serial_number,self.project.name)

# Model to track users on all of the Projects
class User(models.Model):
    name = models.CharField( max_length = 100, )
    email = models.EmailField( max_length = 254, )
    company = models.CharField( max_length = 100, )
    comment = models.CharField( max_length = 140, )

    def __unicode__(self):
        return 'Name: %s - Email: %s - Company: %s' % (self.name, self.email, self.company)

# Relational table to track which users are a part of which projects
class Proj_Has_Users(models.Model):
    project = models.ForeignKey('Project')
    user = models.ForeignKey('User')
    role = models.CharField( max_length = 100, )

    def __unicode__(self):
        return 'Project: %s - User: %s / %s' % (self.project.name, self.user.name, self.user.email)

# Model to track the resource allocation of different hardware
class Resources(models.Model):
    hardware = models.ForeignKey('Hardware')
    cpu = models.CharField( max_length = 25, blank = True, )
    storage = models.CharField( max_length = 25, blank = True,  )
    memory = models.CharField( max_length = 25, blank = True, )

    def __unicode__(self):
        return 'eITMS: %s - Model: %s - CPU: %s - Storage: %s - Memory: %s' % (self.hardware.eITMS_code, self.hardware.model_code, self.cpu, self.storage, self.memory)
