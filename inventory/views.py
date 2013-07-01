from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from inventory.models import Hardware, Project, User, Proj_Has_Users, Resources
from django.contrib import databrowse

databrowse.site.register(Hardware, Project, User, Proj_Has_Users, Resources)

#############DELETE VIEWS######################

class DeleteUserView(DeleteView):
    model = User
    template_name = 'delete-user.html'

    def get_success_url(self):
        return reverse('list-user')


class DeleteUserRelView(DeleteView):
    model = Proj_Has_Users
    template_name = 'delete-userrel.html'

    def get_success_url(self):
        return reverse('list-userrel')


class DeleteResourcesView(DeleteView):
    model = Resources
    template_name = 'delete-resources.html'

    def get_success_url(self):
        return reverse('list-resources')


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

##########LIST VIEWS##############

class ListHardwareView(ListView):
    model = Hardware
    template_name = 'list-hardware.html'


class ListUserView(ListView):
    model = User
    template_name = 'list-user.html'


class ListUserRelView(ListView):
    model = Proj_Has_Users
    template_name = 'list-userrel.html'


class ListResourcesView(ListView):
    model = Resources
    template_name = 'list-resources.html'


class ListProjectView(ListView):
    model = Project
    template_name = 'list-project.html'
    def get_context_data(self, **kwargs):
        context = super(ListProjectView, self).get_context_data(**kwargs)
        context['hardware_list'] = Hardware.objects.all()
        return context

#############CREATE VIEWS######################

class CreateUserView(CreateView):
    model = User
    template_name = 'edit-user.html'

    def get_success_url(self):
        return reverse('list-user')

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('new-user')
        return context


class CreateUserRelView(CreateView):
    model = Proj_Has_Users
    template_name = 'edit-userrel.html'

    def get_success_url(self):
        return reverse('list-userrel')

    def get_context_data(self, **kwargs):
        context = super(CreateUserRelView, self).get_context_data(**kwargs)
        context['action'] = reverse('new-userrel')
        return context


class CreateResourcesView(CreateView):
    model = Resources
    template_name = 'edit-resources.html'

    def get_success_url(self):
        return reverse('list-resources')

    def get_context_data(self, **kwargs):
        context = super(CreateResourcesView, self).get_context_data(**kwargs)
        context['action'] = reverse('new-resources')
        return context


class CreateProjectView(CreateView):
    model = Project
    template_name = 'edit-project.html'

    def get_success_url(self):
        return reverse('list-project')

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('new-project')
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

##########UPDATE VIEWS####################333

class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'edit-project.html'

    def get_success_url(self):
        return reverse('list-project')

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-project', kwargs={'pk': self.get_object().id})
        return context


class UpdateUserView(UpdateView):
    model = User
    template_name = 'edit-user.html'

    def get_success_url(self):
        return reverse('list-user')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-user', kwargs={'pk': self.get_object().id})
        return context


class UpdateUserRelView(UpdateView):
    model = Proj_Has_Users
    template_name = 'edit-userrel.html'

    def get_success_url(self):
        return reverse('list-userrel')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserRelView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-userrel', kwargs={'pk': self.get_object().id})
        return context


class UpdateResourcesView(UpdateView):
    model = Resources
    template_name = 'edit-resources.html'

    def get_success_url(self):
        return reverse('list-resources')

    def get_context_data(self, **kwargs):
        context = super(UpdateResourcesView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-resources', kwargs={'pk': self.get_object().id})
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
