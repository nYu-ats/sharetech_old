
from sharetech.forms.UserCreateForm import UserCreateForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired , loads, dumps
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

# ユーザーモデル(カスタム)取得
User = get_user_model()

class UserCreateView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'sharetech/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email_verified_at = None
        user.save()

        # アクティベーションurl送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol' : self.request.scheme,
            'domain' : domain,
            'token' : dumps(user.pk),
            'user' : user,
        }

        subject = render_to_string('sharetech/mail_template/create/subject_register_done.txt', context)
        message = render_to_string('sharetech/mail_template/create/register_done.txt', context)

        user.email_user(subject, message)
        return redirect('register_done')

user_create = UserCreateView.as_view()