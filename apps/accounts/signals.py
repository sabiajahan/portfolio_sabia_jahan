from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.accounts.models import UserProfile


# Signal handler for user creation and update
@receiver(post_save, sender=get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create the profile only if it's a new user
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Save the profile if the user already exists (this can be used to update profile information)
        if hasattr(instance, 'profile'):
            instance.profile.save()