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
    
    # View list of Projects
    url(r'^listu$', inventory.views.ListUserView.as_view(), name='list-user',), 
    # Edit view of Projects
    url(r'^editu/(?P<pk>\d+)/$', inventory.views.UpdateUserView.as_view(), name='edit-user',),
    # Create view of Project
    url(r'^newu$', inventory.views.CreateUserView.as_view(), name='new-user',),
    # Delete view of Hardware
    url(r'^deleteu/(?P<pk>\d+)/$', inventory.views.DeleteUserView.as_view(), name='delete-user',),

    # View list of Projects
    url(r'^listur$', inventory.views.ListUserRelView.as_view(), name='list-userrel',), 
    # Edit view of Projects
    url(r'^editur/(?P<pk>\d+)/$', inventory.views.UpdateUserRelView.as_view(), name='edit-userrel',),
    # Create view of Project
    url(r'^newur$', inventory.views.CreateUserRelView.as_view(), name='new-userrel',),
    # Delete view of Hardware
    url(r'^deleteur/(?P<pk>\d+)/$', inventory.views.DeleteUserRelView.as_view(), name='delete-userrel',),

    # View list of Projects
    url(r'^listr$', inventory.views.ListResourcesView.as_view(), name='list-resources',), 
    # Edit view of Projects
    url(r'^editr/(?P<pk>\d+)/$', inventory.views.UpdateResourcesView.as_view(), name='edit-resources',),
    # Create view of Project
    url(r'^newr$', inventory.views.CreateResourcesView.as_view(), name='new-resources',),
    # Delete view of Hardware
    url(r'^deleter/(?P<pk>\d+)/$', inventory.views.DeleteResourcesView.as_view(), name='delete-resources',),
)
