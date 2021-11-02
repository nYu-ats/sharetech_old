from django import forms
from sharetech.models.User import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        # ユーザーモデルのemailとpasswordフィールドのみを使用
        fields = ['email', 'password']
        field_order = ['email', 'password']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        # 親クラスのコンストラクタを先に呼び出さなければ、widgetの設定がうまくいかない
        super().__init__(*args, **kwargs)
        # email認証だが、AuthenticationFormの仕様上usernameで指定が必要
        self.fields['username'].widget = forms.EmailInput(attrs={'placeholder':'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'Password'})