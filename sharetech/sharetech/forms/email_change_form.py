import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password
from sharetech.validators.custom_validator import email_validate
from sharetech.constants.messages import ErrorMessage

class EmailChangeForm(ModelForm):
    '''
    メールアドレス変更用フォーム
    '''

    class Meta:
        model = CustomUser
        fields = {
            'tmp_email',
        }
        labels = {
            'tmp_email': '新しいメールアドレス',
        }
    
    email_confirm = forms.CharField(
        label = 'メールアドレス再入力',
        required = True,
        strip = False,
        widget = forms.EmailInput(attrs={'type':'email'}),
    )

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # エラーメッセージ変更のため、defaultのvalidatorを上書き
        self.fields['tmp_email'].validators = [email_validate]
    
    def clean(self):
        super().clean()
        email = self.cleaned_data.get('tmp_email')
        email_confirm = self.cleaned_data.get('email_confirm')

        if email != email_confirm:
            raise forms.ValidationError(ErrorMessage().failuer_email_match)
