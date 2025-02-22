from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin

# Define a custom UserAdmin to manage the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register CustomUser with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)

# Register UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user', 'bio', 'birth_date', 'profile_picture', 'address')
    search_fields = ('user__username', 'bio')

admin.site.register(UserProfile, UserProfileAdmin)