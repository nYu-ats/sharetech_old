from django.contrib.auth.views import LoginView as AuthLoginView
from ..forms.LoginForm import LoginForm

class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'sharetech/login.html'

auth_login = LoginView.as_view()