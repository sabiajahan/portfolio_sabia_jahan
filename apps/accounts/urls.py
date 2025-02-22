# apps/accounts/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [

    
    path('profile/', views.user_profile, name='account_profile'),  # Add the user profil
    path('account/settings/', TemplateView.as_view(template_name="account/account_settings.html"), name='account_settings'),
    path('profile/update/', views.UserProfileUpdateView.as_view(), name='profile_update'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
