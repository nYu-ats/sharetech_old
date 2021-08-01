from django.db.models import fields
from django.forms import widgets
from django import forms
from sharetech.models.User import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']
        field_order = ['email', 'password']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # email認証だが、usernameで指定が必要
        self.fields['username'].widget = forms.EmailInput(attrs={'placeholder':'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'Password'})