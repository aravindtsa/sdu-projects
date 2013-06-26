from django.db import models
from django.core.urlresolvers import reverse

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
#		return ' - '.join([
#				'eITMS:' + self.eITMS_code,
#				'model:' + self.model_code,
#				's/n:' + self.serial_number,
#				'project:' + self.project_id,
#			])

class Project(models.Model):
    name = models.CharField( max_length = 50, unique = True, )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField( max_length = 50, )
    information = models.CharField( max_length = 300, )

    def __unicode__(self):
        return self.name
