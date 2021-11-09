from django.contrib.auth.views import LoginView as AuthLoginView
from ..forms.login_form import LoginForm

class LoginView(AuthLoginView):
    '''
    ログイン処理
    '''
    # ログインフォーム
    authentication_form = LoginForm
    # ログイン画面テンプレート
    template_name = 'sharetech/login.html'

auth_login = LoginView.as_view()