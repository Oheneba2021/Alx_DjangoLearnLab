from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",{
                "fields": (
                    "date_of_birth",
                    "profile_photo",
                )
            }
        )
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",{
                "fields": (
                    "date_of_birth",
                    "profile_photo",
                )
            }
        )
    )
    
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        # "date_of_birth",
    )

# Register your models here.
