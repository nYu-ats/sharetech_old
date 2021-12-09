from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.utils.model_template_adapter import ConsultWindodwAdapter
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from django.views import generic
from sharetech.forms.profile_edit_form import ProfileEditForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from .base_page_common_view import BasePageCommonView

User = get_user_model()

class ProfileEditView(BasePageCommonView, generic.UpdateView):
    '''
    プロフィール編集画面
    '''
    model = User
    form_class = ProfileEditForm
    template_name = 'sharetech/profile_edit.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # プロフィール更新対象としてログインユーザー情報を初期セット
        return queryset.filter(email = self.request.user)
        
    # エラー時にformを引数で受け取るため、**kwawrgsが必要    
    # メールアドレス変更ページ遷移のため、ユーザーidをtemplateに埋め込む必要あり
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_id'] = User.objects.get(email=self.request.user).id
        # ユーザーアイコン及び申込状況の設定
        context.update(self.prepare()._base_context_dict)
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.updated_at = timezone.now()
        user.save()

        return redirect('profile_edit_complete')

profile_edit = ProfileEditView.as_view()