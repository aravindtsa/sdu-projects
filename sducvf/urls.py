from django.conf.urls import patterns, include, url
from django.contrib import databrowse
import inventory.views

urlpatterns = patterns('',
	# View list of Hardware
	url(r'^listh$', inventory.views.ListHardwareView.as_view(), name='list-hardware',), 
	# Edit view of Hardware
	url(r'^edith/(?P<pk>\d+)/$', inventory.views.UpdateHardwareView.as_view(), name='edit-hardware',),
	# Create view of Hardware
	url(r'^newh$', inventory.views.CreateHardwareView.as_view(), name='new-hardware',),
	# Delete view of Hardware
	url(r'^deleteh/(?P<pk>\d+)/$', inventory.views.DeleteHardwareView.as_view(), name='delete-hardware',),
	# Databrowse
	url(r'^databrowse/(.*)', databrowse.site.root),

	# View list of Projects
	url(r'^listp$', inventory.views.ListProjectView.as_view(), name='list-project',), 
	# Edit view of Projects
	url(r'^editp/(?P<pk>\d+)/$', inventory.views.UpdateProjectView.as_view(), name='edit-project',),
	# Create view of Project
	url(r'^newp$', inventory.views.CreateProjectView.as_view(), name='new-project',),
	# Delete view of Hardware
	url(r'^deletep/(?P<pk>\d+)/$', inventory.views.DeleteProjectView.as_view(), name='delete-project',),
)
