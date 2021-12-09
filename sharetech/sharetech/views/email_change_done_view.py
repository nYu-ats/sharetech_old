from django.views import generic

class EmailChangeDoneView(generic.TemplateView):

    template_name = 'sharetech/message.html'

    def get_context_data(self):
        context = super().get_context_data()
        # TODO メッセージは1ファイルで管理するようにする
        context['message'] = '新しいメールアドレスに認証URLを送信しました。<br>ご確認の上、添付のURLにアクセスしてください。'
        return context

email_change_done = EmailChangeDoneView.as_view()