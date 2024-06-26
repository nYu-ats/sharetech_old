from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from sharetech.utils import ConvertChoiceFieldDisplay
import re
from sharetech.constants.messages import ErrorMessage, RePatterns
from sharetech.models import (
    CustomUser,
    IndustryMst,
    OccupationMst,
    PositionMst,
)

class ProfileEditForm(ModelForm):
    '''
    プロフィール編集フォーム
    '''

    __IMG_SIZE = 2*1000*1000

    # ドロップダウンリストに書くモデル名称が表示されるよう変換
    industry_id = ConvertChoiceFieldDisplay(
        queryset = IndustryMst.objects.all(),
        empty_label='業種を選択してください',
        label = '業種'
        )
    occupation_id = ConvertChoiceFieldDisplay(
        queryset = OccupationMst.objects.all(),
        empty_label='職種を選択してください',
        label = '職種'
        )
    position_id = ConvertChoiceFieldDisplay(
        queryset = PositionMst.objects.all(),
        empty_label='役職を選択してください',
        label = '役職'
        )
    
    # 自己紹介と実績は文字数が多いためtextareaに変更
    introduction = forms.CharField(
        widget = forms.Textarea,
        label = '自己紹介',
    )
    archivement = forms.CharField(
        widget = forms.Textarea,
        label = '実績',
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
            'industry_id', 
            'occupation_id', 
            'position_id',
            'icon_path',
            'introduction',
            'archivement',
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
        self.fields['industry_id'].required = False
        self.fields['occupation_id'].required = False
        self.fields['position_id'].required = False
        self.fields['icon_path'].required = False
        self.fields['introduction'].required = False
        self.fields['archivement'].required = False
        self.fields['company'].required = False
        
        # 画面で画像アップロードのスタイル変更
        self.fields['icon_path'].widget.attrs['id'] = 'file'
        self.fields['icon_path'].widget.initial_text = ''
        self.fields['icon_path'].widget.input_text = ''

        # 自己紹介と実績は文字数が多いためtextareaに変更
        self.fields['introduction'].widget.attrs.update({
            'cols': '32',
            'rows': '16',
        })
        self.fields['archivement'].widget.attrs.update({
            'cols': '32',
            'rows': '16',
        })

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

    def clean_icon_path(self):
        # ファイルサイズ制限
        icon_path = self.cleaned_data.get('icon_path')

        if icon_path and icon_path.size > self.__IMG_SIZE:
            raise forms.ValidationError(
                '画像サイズが大きすぎます。%sMBより小さいサイズの画像をお願いします。' \
                % str(self.__IMG_SIZE//1000//1000)
            )

        return icon_path
