from django.shortcuts import redirect
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from django.views import generic
from sharetech.forms.consult_window_edit_form import ConsultWindowEditForm
from sharetech.models.category_consult_window_mapping import CategoryConsultWindowMapping
from django.utils import timezone
from .base_page_common_view import BasePageCommonView

class ConsultWindowUpdateView(BasePageCommonView, generic.UpdateView):
    '''
    相談窓口更新
    '''

    model = ConsultWindow
    form_class = ConsultWindowEditForm
    template_name = 'sharetech/consult_window_edit.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # url patternでのパラメータ受け取りkeyは'pk'で指定しないとエラーとなる
        # 無理矢理requestから取り出しているが、たぶん正規の取り出し方がある
        return queryset.filter(id = self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # 選択済みのカテゴリはチェックを入れる
        category_mapping_list = list(
            CategoryConsultWindowMapping.objects.filter(
                consult_window_id = self.kwargs.get('pk'),
                is_deleted = False)
            )

        context['checked_list'] = [category_mapping.category_id.id for category_mapping in category_mapping_list]
        context.update(self.prepare().set_category_dict())
        # 削除ボタン制御用フラグ
        context['is_deletable'] = 1
        return context

    def form_valid(self, form):
        consult_window_id = self.kwargs.get('pk')

        if 'delete_flg' not in self.request.POST:

            consult_window = form.save(commit=False)
            consult_window.updated_at = timezone.now()
            consult_window.save()

            # カテゴリマッピングの更新
            # モデルデータとの比較のためintにキャスト
            new_categories = self.request.POST.getlist('category')
            new_categories = [int(category) for category in new_categories]
            current_categories = list(CategoryConsultWindowMapping.objects.filter(consult_window_id = consult_window_id))
            
            # 新規作成・更新対象の仕分け
            create_list = [
                category_id for category_id in new_categories 
                if category_id not in [current_category.category_id.id for current_category in current_categories]
                ]
            # 更新・削除対象はmodelオブジェクトのリストとして保持
            # 過去未登録->削除されてレコードが再登録される場合は、レコード削減のため削除フラグで調整する
            reopen_list = [
                category for category in current_categories
                if category.category_id.id in new_categories and category.is_deleted == True
            ]
            delete_list = [
                category for category in current_categories
                if category.category_id.id not in new_categories
            ]

            # DB操作
            create_category_mapping = []
            for category_id in create_list:
                category = CategoryConsultWindowMapping(
                    category_id = CategoryMst.objects.get(id = category_id),
                    consult_window_id = ConsultWindow.objects.get(id = consult_window_id)
                )
                create_category_mapping.append(category)
            CategoryConsultWindowMapping.objects.bulk_create(create_category_mapping)

            for category_model in reopen_list:
                category_model.is_deleted = False
            CategoryConsultWindowMapping.objects.bulk_update(reopen_list, fields=['is_deleted'])

            for category_model in delete_list:
                category_model.is_deleted = True
            CategoryConsultWindowMapping.objects.bulk_update(delete_list, fields=['is_deleted'])
        else:
            # 相談窓口の削除
            targetConsultWindow = ConsultWindow.objects.get(id = consult_window_id)
            targetConsultWindow.is_deleted = True
            targetConsultWindow.save()

        return redirect('consult_window_edit_complete')

consult_window_update = ConsultWindowUpdateView.as_view()