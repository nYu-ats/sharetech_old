from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
import re
from sharetech.constants.messages import ErrorMessage, RePatterns
from sharetech.models import (
    ConsultWindow,
)

class ConsultWindowEditForm(ModelForm):
    '''
    相談窓口作成・編集
    '''

    consult_window_overview = forms.CharField(
        widget = forms.Textarea,
        label = '概要',
        required = True,
    )
    archivement = forms.CharField(
        widget = forms.Textarea,
        label = '実績',
        required = True,
    )

    class Meta:
        model = ConsultWindow
        fields = {
            'consult_window_title',
            'consult_window_overview',
            'archivement',
            'scheduler_url',
            'consult_price',
        }
        labels={
            'consult_window_title': 'タイトル',
            'scheduler_url': 'スケジューラー調整リンク',
            'consult_price': '設定料金',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        # 料金は12/22時点では設定不可だが、項目だけ用意しておく
        self.fields['consult_price'].widget.attrs['readonly'] = 'readonly'
        self.fields['consult_price'].initial = '0'

        # 自己紹介と実績は文字数が多いためtextareaに変更
        self.fields['consult_window_overview'].widget.attrs.update({
            'cols': '32',
            'rows': '16',
        })
        self.fields['archivement'].widget.attrs.update({
            'cols': '32',
            'rows': '16',
        })
        # 以下必須入力
        self.fields['consult_window_title'].required = True
        self.fields['scheduler_url'].required = True
        self.fields['consult_price'].required = True        

    def clean(self):
        super().clean()
    
    def clean_scheduler_url(self):
        # URLフォーマットチェック
        scheduler_url = self.cleaned_data.get('scheduler_url')
        if not re.match(RePatterns().scheduler_url_pattern, scheduler_url):
            raise forms.ValidationError(ErrorMessage().failuer_scheduler_url_pattern)
        
        return scheduler_url