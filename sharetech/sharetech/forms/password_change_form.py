import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms

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
        self.fields['password'].widget = forms.PasswordInput(attrs={'value':''})
        self.fields['new_password'].widget = forms.PasswordInput(attrs={'type':'password'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={'type':'password'})

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if  new_password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password')
        if len(password) < 8:
            raise ValidationError('パスワードは8文字以上で設定してください')
        elif len(password) > 20:
            raise ValidationError('パスワードは20文字以下で設定してください')
        return password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('パスワードは8文字以上で設定してください')
        elif len(password) > 20:
            raise ValidationError('パスワードは20文字以下で設定してください')
        return password
