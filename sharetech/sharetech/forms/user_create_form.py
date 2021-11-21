import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password

class UserCreateForm(ModelForm):
    '''
    ユーザー新規登録用フォーム
    '''

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
            'industry_id', 
            'occupation_id', 
            'position_id',
            'password', 
            ]

    password_confirm = forms.CharField(
        label = '確認用パスワード',
        required = True,
        strip = False,
        widget = forms.PasswordInput(attrs={'type':'password'}),
    )

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password'})

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