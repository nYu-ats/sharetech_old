from django.views import generic
from sharetech.constants.messages import GeneralMessages

class PasswordChangeCompleteView(generic.TemplateView):
    
    template_name = 'sharetech/message.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['message'] = GeneralMessages().change_password
        # ユーザーアイコン非表示にするため、ログアウト状態を画面に渡す
        context['logout'] = True
        return context

password_change_complete = PasswordChangeCompleteView.as_view()