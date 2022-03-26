from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User
from .forms import UserChangeForm, ProfileForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user', 'active']
    search_fields = ('first_name',)
    form = ProfileForm
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'is_active', ]

    model = User
    form = UserChangeForm