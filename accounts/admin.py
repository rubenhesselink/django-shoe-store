from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import cUserCreationForm, cUserChangeForm
from . models import cUser


class cUserAdmin(UserAdmin):
    add_form     = cUserCreationForm
    form         = cUserChangeForm
    model        = cUser
    list_display = [
        'email',
        'username',
    ] 

admin.site.register(cUser, cUserAdmin)