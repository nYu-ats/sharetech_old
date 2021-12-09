from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class ProfileEditCompleteView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'sharetech/message.html'
    
    def get_context_data(self):
        context = super().get_context_data(**kwargs)
        # TODO メッセージは1ファイルで管理するようにする
        context['message'] = 'プロフィール編集が完了しました'
        return context

profile_edit_complete = ProfileEditCompleteView.as_view()