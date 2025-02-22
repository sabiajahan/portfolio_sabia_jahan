from .models import SoftwareInfo

def software_info(request):
    """
    A context processor to inject software information into templates.
    """
    software_info = SoftwareInfo.objects.filter(status='Active').first()
    
    if software_info:
        return {
            'software_name': software_info.software_name,
            'software_title': software_info.software_title or 'No Title Available',
            'software_contact': software_info.software_contact or 'No Contact Available',
            'software_email': software_info.software_email or 'No Email Available',
            'software_address': software_info.software_address or 'No Address Available',
            'software_dev_by': software_info.software_dev_by or 'No Footer Available',
            'software_logo': software_info.software_logo.url if software_info.software_logo else None,
            'software_favicon': software_info.software_favicon.url if software_info.software_favicon else None,
        }
    else:
        return {
            'software_name': 'No Available Software Info',
            'software_title': 'No Title Available',
            'software_contact': 'No Contact Available',
            'software_email': 'No Email Available',
            'software_address': 'No Address Available',
            'software_dev_by': 'No Footer Available',
            'software_logo': None,
            'software_favicon': None,
        }