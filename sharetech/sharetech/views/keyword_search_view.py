from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from sharetech.models.consult_window import ConsultWindow
from sharetech.utils.model_template_adapter import (ConsultWindodwAdapter, CategoryAdapter)
from sharetech.models.category_mst import CategoryMst
from enum import IntEnum

class KeyWordSearchView(View):
    '''
    キーワード検索
    '''
    class DisplayNum(IntEnum):
        # 各抽出記事抽出数設定用Enum
        SMALL = 12
        STANDARD = 24
        LARGE = 36

    def get(self, request, *args, **kwargs):
        # カテゴリ取得
        category_list = list(CategoryMst.objects.filter(category_hierarchy=2).order_by('category_hierarchy'))

        # TODO 検索ロジック検討
        keyword = self.request.GET.get('search_key')
        article_window_list = list(ConsultWindow.objects.filter(
            Q(consult_window_title__icontains = keyword) | 
            Q(consult_window_overview__icontains = keyword) |
            Q(archivement__icontains = keyword)
        ).order_by('created_at')[:self.DisplayNum.SMALL])

        keyword_filtered = {
            'keyword' : keyword,
            'keyword_filterd' : ConsultWindodwAdapter.convert_to_template_context(article_window_list),
            'category_dict' : CategoryAdapter.convert_to_template_context(category_list),
        }        

        return render(request, 'sharetech/top.html', keyword_filtered)

keyword_search = KeyWordSearchView.as_view()