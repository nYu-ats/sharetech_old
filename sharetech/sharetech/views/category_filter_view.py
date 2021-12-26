from django.shortcuts import render
from sharetech.models.category_consult_window_mapping import CategoryConsultWindowMapping
from sharetech.models.category_mst import CategoryMst
from sharetech.models.consult_window import ConsultWindow
from .base_page_common_view import BasePageCommonView

class CategoryFilterView(BasePageCommonView):
    '''
    カテゴリ検索
    '''

    def get(self, request, *args, **kwargs):
        select_category_id = ''
        if 'category_id' in kwargs:
            select_category_id = kwargs['category_id']
        
        category_name = CategoryMst.objects.get(id=select_category_id).category_name
        target_id_list = [model.consult_window_id.id for model in list(CategoryConsultWindowMapping.objects.filter(category_id = select_category_id, is_deleted = False))]

        consult_window_list = list(
            ConsultWindow.objects.filter(
                pk__in = target_id_list,
                is_deleted = False
                ).order_by('created_at')[:self.DisplayNum.SMALL]
            )
        
        self.prepare().set_category_dict().update(
            {
            'category_name' : category_name,
            'category_filterd' : self.create_consult_window_list(consult_window_list),
            }
        )

        return render(request, self._template, self._base_context_dict)

category_filter = CategoryFilterView.as_view()