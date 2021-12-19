from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from .base_page_common_view import BasePageCommonView
from enum import IntEnum

class KeyWordSearchView(BasePageCommonView):
    '''
    キーワード検索
    '''

    def get(self, request, *args, **kwargs):
        # TODO 検索ロジック検討
        keyword = self.request.GET.get('search_key')
        article_window_list = list(ConsultWindow.objects.filter(
            Q(consult_window_title__icontains = keyword) | 
            Q(consult_window_overview__icontains = keyword) |
            Q(archivement__icontains = keyword)
        ).order_by('created_at')[:self.DisplayNum.SMALL])

        self.prepare().set_category_dict().update(
            {
            'keyword' : keyword,
            'keyword_filterd' : self.create_consult_window_list(article_window_list),
            }
        )

        return render(request, self._template, self._base_context_dict)

keyword_search = KeyWordSearchView.as_view()