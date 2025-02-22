from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _



#NOTE:==========| Time Stamped Models Here |==========
#NOTE:==========| Time Stamped Models Here |==========
class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created', verbose_name='Created By')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated', verbose_name='Updated By')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deleted At')
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_deleted', verbose_name='Deleted By')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP Address')

    class Meta:
        abstract = True


#NOTE:==========| Non Deleted Manager Models Here |==========
class NonDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)




#NOTE:==========| Software Info Models Here |==========
class SoftwareInfo(TimeStamped):
    YES_NO_CHOICES = [('Active', 'Active'), ('Deactivated', 'Deactivated'),]
    
    software_name = models.CharField(max_length=255)
    software_title = models.CharField(max_length=255)
    software_email = models.EmailField(max_length=255, verbose_name=_("Email"), null=True, blank=True)
    software_contact = models.CharField(max_length=15, verbose_name=_("Contact"), null=True, blank=True)
    software_address = models.TextField(verbose_name=_("Address"), null=True, blank=True)
    software_dev_by = models.CharField(max_length=255)
    software_logo = models.ImageField(upload_to='software_logos/', blank=True, null=True)
    software_favicon = models.ImageField(upload_to='software_favicons/', blank=True, null=True)
    status = models.CharField(max_length=15, choices=YES_NO_CHOICES, default='Active', verbose_name='Status') 

    objects = NonDeletedManager()  # Default manager to exclude deleted items

    #NOTE:==========| Soft Delete Method Here |==========
    def delete(self, user=None, ip_address=None):
        self.deleted_at = now()
        self.deleted_by = user
        self.ip_address = ip_address
        self.save()

    def __str__(self):
        return f"{self.software_name}"

    class Meta:
        verbose_name = 'Software Info'
        verbose_name_plural = 'Software Info'
        ordering = ['-software_name']
        db_table = 'SOFTWARE_INFO'