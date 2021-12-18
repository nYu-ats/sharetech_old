from sharetech.forms.user_create_form import UserCreateForm
from root import settings
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import dumps
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

class UserCreateView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'sharetech/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        # パスワードハッシュ化
        user.password = make_password(form.cleaned_data.get('password'))
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
        from_email = settings.EMAIL_HOST_USER
        to = [user.email]
        send_mail(subject, message, from_email, to)
        return redirect('register_done')

user_create = UserCreateView.as_view()