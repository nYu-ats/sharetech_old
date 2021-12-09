import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password

class EmailChangeForm(ModelForm):
    '''
    メールアドレス変更用フォーム
    '''

    class Meta:
        model = CustomUser
        fields = {
            'tmp_email',
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
    
    def clean(self):
        super().clean()