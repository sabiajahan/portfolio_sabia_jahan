from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SoftwareInfo
from .forms import SoftwareInfoForm
from apps.dashboard.mixins import SuperUserRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from apps.dashboard.mixins import CreateUserMixin, UpdateUserMixin, DeleteUserMixin



#NOTE:==========| Dashboard Views Here |==========
class DashboardView(LoginRequiredMixin, SuperUserRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    


#NOTE:==========| Software Info List Views Here |==========
class SoftwareInfoListView(LoginRequiredMixin, SuperUserRequiredMixin, ListView):
    model = SoftwareInfo
    template_name = 'software_info/software_info_list.html'
    context_object_name = 'software_info_list'

#NOTE:==========| Software Info Create Views Here |==========
class SoftwareInfoCreateView(LoginRequiredMixin, SuperUserRequiredMixin, CreateUserMixin, CreateView):
    model = SoftwareInfo
    form_class = SoftwareInfoForm
    template_name = 'software_info/software_info_form.html'
    success_url = reverse_lazy('software_info_list')

#NOTE:==========| Software Info Update Views Here |==========
class SoftwareInfoUpdateView(LoginRequiredMixin, SuperUserRequiredMixin, UpdateUserMixin, UpdateView):
    model = SoftwareInfo
    form_class = SoftwareInfoForm
    template_name = 'software_info/software_info_form.html'
    success_url = reverse_lazy('software_info_list')

#NOTE:==========| Software Info Delete Views Here |==========
class SoftwareInfoDeleteView(LoginRequiredMixin, SuperUserRequiredMixin, DeleteUserMixin, DeleteView):
    model = SoftwareInfo
    template_name = 'software_info/software_info_confirm_delete.html'
    success_url = reverse_lazy('software_info_list')

