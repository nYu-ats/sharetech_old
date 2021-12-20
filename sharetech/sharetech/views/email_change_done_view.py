from django.views import generic
from sharetech.constants.messages import GeneralMessages

class EmailChangeDoneView(generic.TemplateView):

    template_name = 'sharetech/message.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['message'] = GeneralMessages().change_email
        # ユーザーアイコン非表示にするため、ログアウト状態を画面に渡す
        context['logout'] = True
        return context

email_change_done = EmailChangeDoneView.as_view()