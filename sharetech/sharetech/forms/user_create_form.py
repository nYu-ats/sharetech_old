import django
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password
from sharetech.utils import ConvertChoiceFieldDisplay
from sharetech.models.user import (
    CustomUser,
    IndustryMst,
    OccupationMst,
    PositionMst,
)

class UserCreateForm(ModelForm):
    '''
    ユーザー新規登録用フォーム
    '''
    
    # 確認用パスワードフィールド
    password_confirm = forms.CharField(
        label = 'パスワード再入力',
        required = True,
        strip = False,
        widget = forms.PasswordInput(attrs={'type':'password'}),
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
            ]
        labels = {
            'company': '会社名', 
            'first_name_jp': '名字', 
            'family_name_jp': '氏名', 
            'first_name_en': '名字(ローマ字)', 
            'family_name_en': '氏名(ローマ字)', 
            'email': 'メールアドレス', 
            'role_code': 'ロール選択', 
            'password': 'パスワード', 
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password'})
        # 以下必須でない入力項目
        self.fields['industry_name'].required = False
        self.fields['occupation_name'].required = False
        self.fields['position_name'].required = False

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError('確認用パスワードが一致しません')
    
    def clean_password(self):
        # パスワードチェック
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('パスワードは8文字以上で設定してください')
        elif len(password) > 20:
            raise ValidationError('パスワードは20文字以下で設定してください')
        return password
        
    def clean_email(self):
        # メールアドレスバリデーション
        email = self.cleaned_data.get('email')
        CustomUser.objects.filter(email = email, email_verified_at = None).delete()
        return email