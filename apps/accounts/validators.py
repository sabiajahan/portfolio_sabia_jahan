import re
from django.core.exceptions import ValidationError

def validate_bangladesh_phone_number(value):
    """
    Validate a Bangladeshi phone number in local format (e.g., 01799925246).
    Converts to international format (+8801799925246) for storage.
    """
    value = str(value)  # Ensure the value is a string

    # Check if the phone number is in the local format (11 digits starting with 01)
    if re.match(r'^01[3-9]\d{8}$', value):
        # Convert to international format for storage
        return "+88" + value

    # Raise validation error for invalid formats
    raise ValidationError('Phone number must be in the local format (e.g., 01799925246).')


class StrongPasswordValidator:
    def __init__(self):
        self.min_length = 5
        self.uppercase_required = 1
        self.digits_required = 2

    def validate(self, password, user=None):
        # Check minimum length
        if len(password) < self.min_length:
            raise ValidationError("Password must be at least 5 characters long.")

        # Check for uppercase letters
        if len(re.findall(r'[A-Z]', password)) < self.uppercase_required:
            raise ValidationError("Password must contain at least one uppercase letter.")

        # Check for digits
        if len(re.findall(r'\d', password)) < self.digits_required:
            raise ValidationError("Password must contain at least two digits.")

    def get_help_text(self):
        return (
            "Your password must be at least 5 characters long, "
            "contain at least one uppercase letter, and at least two digits."
        )