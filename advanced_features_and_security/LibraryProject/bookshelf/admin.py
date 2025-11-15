from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# ----------------------------
# Custom User Admin
# ----------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Include the new fields in the admin form
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register CustomUser with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)

# Keep existing Book model registration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
