from django.views.generic import View
from django.utils.timezone import now
from django.contrib import messages
from django.http import HttpResponseRedirect


from django.http import HttpResponseForbidden

class SuperUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class DeleteUserMixin:
    """
    A mixin to handle soft deletion for models with `deleted_at`, `deleted_by`, and `ip_address` fields.
    """
    success_url = None  # Must be defined in the view using this mixin

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.deleted_at = now()
        obj.deleted_by = request.user
        obj.ip_address = self.get_client_ip()
        obj.save()
        messages.success(request, "Deleted successfully (soft delete).")
        return HttpResponseRedirect(self.success_url)

    def get_client_ip(self):
        """
        Retrieve the client's IP address from the request, prioritizing forwarded headers.
        """
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Split on commas and take the first IP, which is the client's public IP
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            # Use REMOTE_ADDR as a fallback
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
    
class CreateUserMixin:
    """
    Mixin to set `created_by` and `ip_address` fields on object creation.
    """

    success_message = "Created successfully."

    def form_valid(self, form):
        # Set the created_by and ip_address fields
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'ip_address'):
            form.instance.ip_address = self.get_client_ip()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_client_ip(self):
        """
        Retrieve the client's IP address from the request, prioritizing forwarded headers.
        """
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Split on commas and take the first IP, which is the client's public IP
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            # Use REMOTE_ADDR as a fallback
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

class UpdateUserMixin:
    """
    Mixin to set `updated_by` and `ip_address` fields on object update.
    """

    success_message = "Updated successfully."

    def form_valid(self, form):
        # Set the updated_by and ip_address fields
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        if hasattr(form.instance, 'ip_address'):
            form.instance.ip_address = self.get_client_ip()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_client_ip(self):
        """
        Retrieve the client's IP address from the request, prioritizing forwarded headers.
        """
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Split on commas and take the first IP, which is the client's public IP
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            # Use REMOTE_ADDR as a fallback
            ip = self.request.META.get('REMOTE_ADDR')
        return ip







