from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserProfileUpdateForm


@login_required  # Ensures that only logged-in users can access this view
def user_profile(request):
    user = request.user
    # Assuming you have a OneToOne relationship between user and UserProfile
    profile, created = UserProfile.objects.get_or_create(user=user)

    # Pass profile data to the template
    return render(request, 'account/profile.html', {
        'profile': profile
    })


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileUpdateForm
    template_name = "account/profile_update.html"
    success_url = reverse_lazy('account_profile')  # Change to your desired URL

    def get_object(self):
        # Ensure the correct profile object is fetched
        return self.request.user.userprofile

