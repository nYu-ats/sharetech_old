from django import forms
from django.forms import Form
from django.forms.fields import EmailField
from sharetech.models.user import CustomUser
from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext_lazy
from django.utils.text import capfirst
from sharetech.constants.messages import ErrorMessage
from sharetech.validators.custom_validator import email_validate

class LoginForm(Form):
    '''
    ログインフォーム
    '''
    email = EmailField(
        widget = forms.EmailInput(
            attrs={'placeholder':'Email', 'autofocus' : True,}),
        label = 'メールアドレス',
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={'placeholder':'Password',}),
            label = 'パスワード',
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        self.email_field = CustomUser._meta.get_field(CustomUser.USERNAME_FIELD)
        self.fields['email'].max_length = self.email_field.max_length or 254
        # エラーメッセージ変更のため、defaultのvalidatorを上書き
        self.fields['email'].validators = [email_validate]
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)
        
    def clean(self):
        # ログインチェック
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(ErrorMessage().failuer_login_auth)
            else:
                if self.user_cache.is_deleted:
                    raise forms.ValidationError(ErrorMessage().failuer_user_not_exist)

    def clean_password(self):
        # パスワードバリデーションチェック
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError(ErrorMessage().failuer_password_length)
        elif len(password) > 20:
            raise forms.ValidationError(ErrorMessage().failuer_password_length)

        return password
    
    def get_user(self):
        # 認証済みのユーザーを返す
        return self.user_cache
