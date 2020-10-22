from django import forms
from django.contrib.auth.models import User


class PermissionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_permissions',)
        labels = {
            'user_permissions': 'Uprawnienia'
        }
        widgets = {
            'user_permissions' : forms.CheckboxSelectMultiple()
        }