from sharetech.forms.user_create_form import UserCreateForm
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
from django.contrib.auth import logout
from sharetech.forms.email_change_form import EmailChangeForm
from .base_page_common_view import BasePageCommonView

User = get_user_model()

class EmailChangeView(BasePageCommonView, generic.UpdateView):
    '''
    メールアドレス変更
    '''
    model = User
    form_class = EmailChangeForm
    template_name = 'sharetech/email_change.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(email = self.request.user)

    # エラー時にformを引数で受け取るため、**kwawrgsが必要
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['current_email'] = User.objects.get(email = self.request.user).email
        # ユーザーアイコン及び申込状況の設定
        context.update(self.prepare()._base_context_dict)
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        # 新規メールアドレスに認証メール送信のため
        new_email = form.cleaned_data.get('tmp_email')
        user.tmp_email = new_email
        user.save()

        # TODO メール送信util化
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
        message = render_to_string('sharetech/mail_template/mail_change/mail_change_done.txt', context)
        from_email = settings.EMAIL_HOST_USER
        to = [new_email]
        # TODO メール送信処理実行(未定義なので、utilあたりにメール送信処理を作る)
        send_mail(subject, message, from_email, to)

        # 新規メールアドレス確認のためログアウトさせる
        logout(self.request)

        return redirect('email_change_done')

email_change = EmailChangeView.as_view()