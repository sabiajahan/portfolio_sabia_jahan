from .models import UserProfile

def user_profile(request):
    """
    A context processor to inject the current user's profile data into templates.
    """
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = None
    else:
        profile = None

    return {
        'user_profile': profile,
    }