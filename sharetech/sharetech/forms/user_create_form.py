import django
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password
from sharetech.constants.messages import ErrorMessage, RePatterns
from sharetech.utils import ConvertChoiceFieldDisplay
from sharetech.validators.custom_validator import email_validate
import re
from sharetech.models import (
    CustomUser,
    IndustryMst,
    OccupationMst,
    PositionMst,
    UserSpecialize,
)

class UserCreateForm(ModelForm):
    '''
    ユーザー新規登録用フォーム
    '''
    
    # パスワードはハッシュかしてDB保存のため、Modelの絡むサイズと画面入力文字数が一致しない
    __MAX_PASSWORD_LENGTH = 20
    
    # 確認用パスワードフィールド
    password_confirm = forms.CharField(
        label = 'パスワード再入力',
        required = True,
        strip = False,
        widget = forms.PasswordInput(attrs={'type':'password'}),
        max_length = __MAX_PASSWORD_LENGTH,
    )

    # 専門分野入力フィールド
    specialize = forms.CharField(
        label = '専門分野',
        required = False,
        strip = False,
        max_length = UserSpecialize._meta.get_field('specialize').max_length,
    )

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
        fields = [
            'username',
            'company', 
            'first_name_jp', 
            'family_name_jp', 
            'first_name_en', 
            'family_name_en', 
            'email', 
            'role_code', 
            'industry_name', 
            'occupation_name', 
            'position_name',
            'password', 
            'specialize',
            ]
        labels = {
            'username': '名前',
            'company': '会社名', 
            'first_name_jp': '名字(カナ)', 
            'family_name_jp': '氏名(カナ)', 
            'first_name_en': '名字(ローマ字)', 
            'family_name_en': '氏名(ローマ字)', 
            'email': 'メールアドレス', 
            'role_code': 'ロール選択', 
            'password': 'パスワード', 
            'specialize': '専門分野',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # エラーメッセージ変更のため、defaultのvalidatorを上書き
        self.fields['email'].validators = [email_validate]
        self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password'})
        # 最大入力文字数設定
        self.fields['password'].widget.attrs['maxlength'] = self.__MAX_PASSWORD_LENGTH
        # 以下必須でない入力項目
        self.fields['industry_name'].required = False
        self.fields['occupation_name'].required = False
        self.fields['position_name'].required = False

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(ErrorMessage().failuer_password_match)
    
    def clean_password(self):
        # パスワードチェック
        password = self.cleaned_data.get('password')
        if not re.match(RePatterns().password_pattern, password):
            raise forms.ValidationError(ErrorMessage().failuer_password_format)

        if len(password) < 8:
            raise ValidationError(ErrorMessage().failuer_password_length)
        elif len(password) > 20:
            raise forms.ValidationError(ErrorMessage().failuer_password_length)
        return password
        
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

