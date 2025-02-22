# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('software-info/', views.SoftwareInfoListView.as_view(), name='software_info_list'),
    path('software-info/create/', views.SoftwareInfoCreateView.as_view(), name='software_info_create'),
    path('software-info/edit/<int:pk>/', views.SoftwareInfoUpdateView.as_view(), name='software_info_edit'),
    path('software-info/delete/<int:pk>/', views.SoftwareInfoDeleteView.as_view(), name='software_info_delete'),
    
]