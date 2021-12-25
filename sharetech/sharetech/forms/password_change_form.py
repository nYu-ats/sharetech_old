from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from sharetech.constants.messages import ErrorMessage, RePatterns
from django.contrib.auth.hashers import check_password
import re

class PasswordChangeForm(ModelForm):
    '''
    パスワード変更フォーム
    '''

    class Meta:
        model = CustomUser
        fields = {
            'password',
        }
        labels = {
            'password': '現在のパスワード',
        }

    new_password = forms.CharField(
        label = '新しいパスワード',
        required = True,
        strip = False,
        widget = forms.PasswordInput(attrs={'type':'password'}),
    )

    confirm_password = forms.CharField(
        label = '新しいパスワード再入力',
        required = True,
        strip = False,
        widget = forms.PasswordInput(attrs={'type':'password'}),
    )

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # パスワードバリデーション用に現在のパスワード取得
        self.current_password = kwargs.get('instance').password
        self.fields['password'].widget = forms.PasswordInput(attrs={'value':''})
        self.fields['new_password'].widget = forms.PasswordInput(attrs={'type':'password'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={'type':'password'})

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if  new_password != confirm_password:
            raise forms.ValidationError(ErrorMessage().failuer_password_match)

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password')
        if not re.match(RePatterns().password_pattern, password):
            raise forms.ValidationError(ErrorMessage().failuer_password_format)

        if len(password) < 8:
            raise forms.ValidationError(ErrorMessage().failuer_password_length)
        elif len(password) > 20:
            raise forms.ValidationError(ErrorMessage().failuer_password_length)
        return password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not check_password(password, self.current_password):
            raise forms.ValidationError(ErrorMessage().failuer_current_password_not_exist)
        
        return password
