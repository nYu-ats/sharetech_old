from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as AuthLoginView
from ..forms.LoginForm import LoginForm
from django.contrib.auth import login, authenticate

class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'sharetech/login.html'
    # def get(self, request, *args, **kwargs):
    #     login_form = LoginForm()
    #     return render(request,  'sharetech/registration/login.html', {'form': login_form})

    # def post(self, request, *args, **kwargs):
    #     login_form = LoginForm(request.POST)
    #     if login_form.is_valid():
    #         user = login_form.save()
    #         login(request, user)
    #         return redirect('/')
    #     else:
    #         return render(request,  'sharetech/registration/login.html', {'form': login_form})

auth_login = LoginView.as_view()