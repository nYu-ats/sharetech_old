from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from sharetech.models.user_specialize import UserSpecialize
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
        self.set_speciarize(context)

        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.updated_at = timezone.now()
        if 'icon_path' in self.request.FILES:
            user.icon_path = self.request.FILES['icon_path']
        print(self.request.FILES)

        user.save()

        # 専門分野のレコードを更新
        specialize_list = self.request.POST.getlist('specialize')
        # 削除処理
        user_specialize_list = list(UserSpecialize.objects.filter(user_id=user))
        for targetModel in user_specialize_list:
            if targetModel.specialize not in specialize_list:
                targetModel.is_deleted = True
                targetModel.save()
        # 新規登録、再登録処理
        for specialize in specialize_list:
            targetModel, result = UserSpecialize.objects.get_or_create(user_id=user, specialize=specialize)
            if not result:
                targetModel.is_deleted = False
                targetModel.save()

        return redirect('profile_edit_complete')
    
    def set_speciarize(self, context):
        user = self.request.user
        specialize_list = list(UserSpecialize.objects.filter(user_id = user, is_deleted=False))
        index = 1
        context['specialize'] = {}
        context['specialize_title'] = '専門分野'

        if len(specialize_list) != 0:
            for specialize_model in specialize_list:
                specialize_id = 'specialize_' + str(index)
                context['specialize'][specialize_id] = specialize_model.specialize
                index += 1
        else:
            # 専門分野を1件も登録していなかった場合は空のinput fieldをセットする
            specialize_id = 'specialize_' + str(index)
            context['specialize'][specialize_id] = ''

profile_edit = ProfileEditView.as_view()