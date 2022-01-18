from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class PasswordResetView(auth_views.PasswordResetView):
    '''
    パスワードリセット画面
    ex) パラメータ例
    email_template_name = 'registration/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    title = _('Password reset')
    token_generator = default_token_generator
    '''

    success_url = reverse_lazy('password_reset_mail_done')
    template_name = 'sharetech/password_reset.html'

password_reset = PasswordResetView.as_view()
