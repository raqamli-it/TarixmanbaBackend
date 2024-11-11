# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Permission
# from django.utils.translation import gettext_lazy as _
# from .forms import CustomUserCreationForm
# # from .models import CustomUser
# from django.contrib.auth.models import User


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "password1", "password2"),
#             },
#         ),
#     )
#     add_form = CustomUserCreationForm
#     list_display = ("id","username", "email", "first_name", "last_name", "is_staff")
#     list_filter = ("is_staff", "is_superuser", "is_active", "groups")
#     search_fields = ("username", "first_name", "last_name", "email")
#     ordering = ("username",)
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )

# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Permission)