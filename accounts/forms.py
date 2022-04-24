from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . models import cUser


class cUserCreationForm(UserCreationForm):

    class Meta:
        model = cUser
        fields = (
            'username',
            'email',
        )


class cUserChangeForm(UserChangeForm):

    class Meta:
        model = cUser
        fields = (
            'username',
            'email',
        )