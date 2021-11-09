import django
from django.core.exceptions import ValidationError
from ..models.user import CustomUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import  UserCreationForm

class UserCreateForm(UserCreationForm):
    '''
    ユーザー新規登録用フォーム
    '''

    class Meta:
        model = CustomUser
        fields = ['company', 'username', 'email', 'role_code', 'password1']
        field_order = ['company', 'username', 'email', 'role_code', 'password']


    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # 不要なパスワードフィールド削除
        del self.fields['password2']
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type':'password'})
        self.fields['role_code'].widget = forms.widgets.Select
        self.fields['role_code'].choices = [('Only View', '1'),('View and Post', '2')]
        self.fields['role_code'] = forms.fields.ChoiceField(
            choices = [('1', 'Only View'), ('2', 'View and Post')],
            widget = forms.widgets.Select,
        )

    def clean_password(self):
        password = self.cleaned_data['password1']
        if len(password) < 8:
            raise ValidationError('パスワードは8文字以上で設定してください')
        elif len(password) > 20:
            raise ValidationError('パスワードは20文字以下で設定してください')
        
        return super(UserCreateForm, self).clean_password1()

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email = email, email_verified_at = None).delete()
        
        return email