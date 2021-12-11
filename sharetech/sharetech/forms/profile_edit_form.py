import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from sharetech.utils import ConvertChoiceFieldDisplay
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
        empty_label='業種を選択してください'
        )
    occupation_name = ConvertChoiceFieldDisplay(
        queryset = OccupationMst.objects.all(),
        empty_label='職種を選択してください'
        )
    position_name = ConvertChoiceFieldDisplay(
        queryset = PositionMst.objects.all(),
        empty_label='役職を選択してください'
        )

    class Meta:
        model = CustomUser
        fields = {
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