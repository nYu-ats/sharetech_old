from django.contrib.auth import views as auth_views

class PasswordResetMailDoneView(auth_views.PasswordResetDoneView):
    '''
    パスワードリセットメール送信完了画面
    ex) パラメータ例
    template_name = 'registration/password_reset_done.html'
    title = _('Password reset sent')
    '''
    template_name = 'sharetech/password_reset_mail_done.html'

password_reset_mail_done = PasswordResetMailDoneView.as_view()
