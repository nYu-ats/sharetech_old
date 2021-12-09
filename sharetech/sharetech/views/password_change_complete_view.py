from django.views import generic

class PasswordChangeCompleteView(generic.TemplateView):
    template_name = 'sharetech/message.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        # TODO メッセージは1ファイルで管理するようにする
        context['message'] = 'パスワード変更が完了しました'
        return context

password_change_complete = PasswordChangeCompleteView.as_view()