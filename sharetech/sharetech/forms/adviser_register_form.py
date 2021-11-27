from django import forms
from django.forms import ModelForm
from django.forms.fields import EmailField
from sharetech.models.consult_window import ConsultWindow
from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext_lazy
from django.utils.text import capfirst

class AdviserRegisterForm(ModelForm):
    '''
    専門家登録窓口フォーム
    '''

    class Meta:
        model = ConsultWindow
        fields = [
            'consult_window_title', 
            'consult_window_overview', 
            'consult_price', 
            'timerex_url', 
            'archivement', 
            ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

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