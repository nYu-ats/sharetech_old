from django import forms
from django.forms import ModelForm
from sharetech.models.consult_window import ConsultWindow

class ConsultWindowRegisterForm(ModelForm):
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
            'timerex_url'
            ]
        widgets = {
            'consult_window_overview': forms.Textarea(), # 相談窓口概要
            'consult_price': forms.TextInput(attrs={'readonly':'readonly'}), # アルファ版のみ相談料金をreadonly
            'archivement': forms.Textarea(), # 実績
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
    
    def get_user(self):
        return self.user_cache
