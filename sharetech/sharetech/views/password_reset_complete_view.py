from django.contrib.auth import views as auth_views

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    '''
    パスワードリセット完了ページ
    ex) パラメータ例
    template_name = 'registration/password_reset_complete.html'
    title = _('Password reset complete')
    '''

    template_name = 'sharetech/password_reset_complete.html'

password_reset_complete = PasswordResetCompleteView.as_view()
