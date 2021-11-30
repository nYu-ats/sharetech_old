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
            'archivement',
            # 'expert_user_id', 
            ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
    
    def get_user(self):
        return self.user_cache