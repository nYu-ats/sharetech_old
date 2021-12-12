from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .base_page_common_view import BasePageCommonView

User = get_user_model()

class ProfileEditCompleteView(BasePageCommonView, generic.TemplateView):
    template_name = 'sharetech/message.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        # TODO メッセージは1ファイルで管理するようにする
        context['message'] = 'プロフィール編集が完了しました'
        # ユーザーアイコン及び申込状況の設定
        context.update(self.prepare()._base_context_dict)
        return context

profile_edit_complete = ProfileEditCompleteView.as_view()