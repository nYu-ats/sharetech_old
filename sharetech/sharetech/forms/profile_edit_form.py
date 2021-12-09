import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password

class ProfileEditForm(ModelForm):
    '''
    プロフィール編集フォーム
    '''

    class Meta:
        model = CustomUser
        fields = {
            'company', 
            'first_name_jp', 
            'family_name_jp', 
            'first_name_en', 
            'family_name_en', 
            'industry_id', 
            'occupation_id', 
            'position_id',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean() 