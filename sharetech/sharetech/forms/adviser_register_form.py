from django import forms
from django.forms import Form
from django.forms.fields import EmailField
from sharetech.models.user import CustomUser
from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext_lazy
from django.utils.text import capfirst

class AdviserRegisterForm(Form):
    '''
    専門家登録窓口フォーム
    '''
    organization = forms.CharField(
        widget = forms.TextInput()
    )
    name = forms.CharField(
        widget = forms.TextInput()
    )
    special = forms.CharField(
        widget = forms.TextInput()
    )
    email = EmailField(
        widget = forms.EmailInput(attrs={'placeholder':'Email', 'autofocus' : True,})
    )

    error_messages = {
        'invalid_login' : gettext_lazy(
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive. "
        ),
        'is_deleted' : gettext_lazy(
            "This account is deleted. ",
        ),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        self.email_field = CustomUser._meta.get_field(CustomUser.USERNAME_FIELD)
        self.fields['email'].max_length = self.email_field.max_length or 254
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)
        
        # TODO 全フォーム要素にセットしたいアトリビュートがあればここでセット
        # for field in self.fields.values():
        #     pass

    def clean(self):
        name = self.cleaned_data.get('name')
        organization = self.cleaned_data.get('organization')
        special = self.cleaned_data.get('special')
        email = self.cleaned_data.get('email')

        # if email is not None and password:
        #     self.user_cache = authenticate(self.request, email=email, password=password)
        #     if self.user_cache is None:
        #         raise self.get_invalid_login_error()
        #     else:
        #         self.confirm_login_allowed(self.user_cache)
    
    # def confirm_login_allowed(self, user):
    #     if user.is_deleted:
    #         raise forms.ValidationError(
    #             self.error_messages['is_deleted'],
    #             code = 'deleted',
    #         )
    
    def get_user(self):
        return self.user_cache
    
    # def get_invalid_login_error(self):
    #     return forms.ValidationError(
    #         self.error_messages['invalid_login'],
    #         code = 'invalid_login',
    #         params = {'username' : gettext_lazy('Email')},
    #     )