from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from inventory.models import Hardware, Project
from django.contrib import databrowse

databrowse.site.register(Hardware, Project)

class DeleteHardwareView(DeleteView):
	model = Hardware
	template_name = 'delete-hardware.html'

	def get_success_url(self):
		return reverse('list-hardware')

class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete-project.html'

    def get_success_url(self):
        return reverse('list-project')

class ListHardwareView(ListView):
	model = Hardware
	template_name = 'list-hardware.html'

class ListProjectView(ListView):
    model = Project
    template_name = 'list-project.html'

class CreateProjectView(CreateView):
    model = Project
    template_name = 'edit-project.html'

    def get_success_url(self):
        return reverse('list-project')

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('new-project')
        return context

class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'edit-project.html'

    def get_success_url(self):
        return reverse('list-project')

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-project', kwargs={'pk': self.get_object().id})
        return context

class CreateHardwareView(CreateView):
	model = Hardware
	template_name = 'edit-hardware.html'
	
	def get_success_url(self):
		return reverse('list-hardware')

	def get_context_data(self, **kwargs):
		context = super(CreateHardwareView, self).get_context_data(**kwargs)
		context['action'] = reverse('new-hardware')
		return context

class UpdateHardwareView(UpdateView):
	model = Hardware
	template_name = 'edit-hardware.html'

	def get_success_url(self):
		return reverse('list-hardware')

	def get_context_data(self, **kwargs):
		context = super(UpdateHardwareView, self).get_context_data(**kwargs)
		context['action'] = reverse('edit-hardware', kwargs={'pk': self.get_object().id})
		return context
