from django.shortcuts import render, redirect
from django.views import View

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sharetech/login.html')

login = LoginView.as_view()



