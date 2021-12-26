from django.shortcuts import render, redirect
from django.views import View
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from sharetech.models.user_specialize import UserSpecialize
from django.views import generic
from sharetech.forms.consult_window_edit_form import ConsultWindowEditForm
from sharetech.models.category_consult_window_mapping import CategoryConsultWindowMapping
from django.contrib.auth import get_user_model
from django.utils import timezone
from .base_page_common_view import BasePageCommonView
from django.conf import settings

class ConsultWindowCreateView(BasePageCommonView, generic.CreateView):
    '''
    相談窓口新規作成
    '''

    form_class = ConsultWindowEditForm
    template_name = 'sharetech/consult_window_edit.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # プロフィール更新対象としてログインユーザー情報を初期セット
        return queryset.filter(email = self.request.user)

    def get_context_data(self, **kwargs):
        # 実績に初期値を設定する
        context = super().get_context_data()
        context.update(self.prepare().set_category_dict())

        # 設定してあればユーザープロフィールから実績を初期値としてセットする
        archivement = CustomUser.objects.get(email=self.request.user).archivement
        if archivement:
            context['form'].fields['archivement'].initial = archivement
        
        context['checked_list'] = []
        # 削除ボタン制御用フラグ
        context['is_deletable'] = 0
        return context

    def form_valid(self, form):
        consult_window = form.save(commit=False)
        consult_window.expert_user_id = self.request.user
        consult_window.save()

        # カテゴリ情報をセットする
        cat_list = self.request.POST.getlist('category')
        cat_mapping_list = []
        for cat_id in cat_list:
            cat_mapping = CategoryConsultWindowMapping(
                category_id = CategoryMst.objects.get(id = int(cat_id)),
                consult_window_id = consult_window,
            )
            cat_mapping_list.append(cat_mapping)
        CategoryConsultWindowMapping.objects.bulk_create(cat_mapping_list)

        return redirect('consult_window_edit_complete')


consult_window_create = ConsultWindowCreateView.as_view()
