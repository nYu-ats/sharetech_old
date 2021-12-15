import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from sharetech.utils import ConvertChoiceFieldDisplay
import re
from sharetech.constants.messages import ErrorMessage, RePatterns
from sharetech.models.user import (
    CustomUser,
    IndustryMst,
    OccupationMst,
    PositionMst,
)

class ProfileEditForm(ModelForm):
    '''
    プロフィール編集フォーム
    '''

    # ドロップダウンリストに書くモデル名称が表示されるよう変換
    industry_name = ConvertChoiceFieldDisplay(
        queryset = IndustryMst.objects.all(),
        empty_label='業種を選択してください',
        label = '業種'
        )
    occupation_name = ConvertChoiceFieldDisplay(
        queryset = OccupationMst.objects.all(),
        empty_label='職種を選択してください',
        label = '職種'
        )
    position_name = ConvertChoiceFieldDisplay(
        queryset = PositionMst.objects.all(),
        empty_label='役職を選択してください',
        label = '役職'
        )

    class Meta:
        model = CustomUser
        fields = {
            'username',
            'company', 
            'first_name_jp', 
            'family_name_jp', 
            'first_name_en', 
            'family_name_en', 
            'industry_name', 
            'occupation_name', 
            'position_name',
            'icon_path',
        }
        labels = {
            'username': '名前',
            'company': '会社名', 
            'first_name_jp': '名字(カナ)', 
            'family_name_jp': '氏名(カナ)', 
            'first_name_en': '名字(ローマ字)', 
            'family_name_en': '氏名(ローマ字)', 
            'icon_path': 'アイコン画像選択',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # 以下必須でない入力項目
        self.fields['industry_name'].required = False
        self.fields['occupation_name'].required = False
        self.fields['position_name'].required = False
        self.fields['icon_path'].required = False

        # 画面で画像アップロードのスタイル変更
        self.fields['icon_path'].widget.attrs['id'] = 'file'
        self.fields['icon_path'].widget.initial_text = ''
        self.fields['icon_path'].widget.input_text = ''

    def clean(self):
        super().clean() 

    def clean_first_name_jp(self):
        # カタカナ名チェック
        first_name_jp = self.cleaned_data.get('first_name_jp')
        katakana = re.compile(RePatterns().kana_pattern)
        
        if not katakana.fullmatch(first_name_jp):
            raise forms.ValidationError(ErrorMessage().failuer_name_kana)
        
        return first_name_jp

    def clean_family_name_jp(self):
        # カタカナ名チェック
        family_name_jp = self.cleaned_data.get('family_name_jp')
        katakana = re.compile(RePatterns().kana_pattern)
        
        if not katakana.fullmatch(family_name_jp):
            raise forms.ValidationError(ErrorMessage().failuer_name_kana)

        return family_name_jp

    def clean_first_name_en(self):
        # ローマ字名チェック
        first_name_en = self.cleaned_data.get('first_name_en')
        roma = re.compile(RePatterns().roma_pattern)
        
        if not roma.fullmatch(first_name_en):
            raise forms.ValidationError(ErrorMessage().failuer_name_roma)

        return first_name_en

    def clean_family_name_en(self):
        # ローマ字名チェック
        family_name_en = self.cleaned_data.get('family_name_en')
        roma = re.compile(RePatterns().roma_pattern)
        
        if not roma.fullmatch(family_name_en):
            raise forms.ValidationError(ErrorMessage().failuer_name_roma)

        return family_name_en
