from django.contrib.auth import views as auth_views

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    '''
    パスワードリセット確認ページ
    ex) パラメータ例
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'registration/password_reset_confirm.html'
    title = _('Enter new password')
    token_generator = default_token_generator
    '''
    
    template_name = 'sharetech/password_reset_confirm.html'

password_reset_confirm = PasswordResetConfirmView.as_view()
