from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser,CustomUserAdmin)
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
        "date_of_birth",
    )

# Register your models here.


@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year','author')
    search_fields = ('title', 'author')
# Register your models here.

# @admin.register(CustomUser,CustomUserAdmin)