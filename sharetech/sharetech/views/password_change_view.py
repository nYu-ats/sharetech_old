from sharetech.forms.password_change_form import PasswordChangeForm
from root import settings
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired , loads, dumps
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

User = get_user_model()

class PasswordChangeView(LoginRequiredMixin, generic.UpdateView):
    '''
    パスワード変更
    '''
    model = User
    form_class = PasswordChangeForm
    template_name = 'sharetech/password_change.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(email=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data.get('new_password'))
        user.save()
        logout(self.request)

        return redirect('password_change_complete')

password_change = PasswordChangeView.as_view()