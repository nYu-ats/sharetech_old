from django import forms
from django.forms import ModelForm
from sharetech.models.consult_window import ConsultWindow

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
            ]
        widgets = {
            'consult_window_overview': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
    
    def get_user(self):
        return self.user_cache
