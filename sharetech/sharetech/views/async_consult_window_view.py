from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from enum import IntEnum
from .base_page_common_view import BasePageCommonView

class AsyncArticleLoadView(BasePageCommonView):
    class LoadNum(IntEnum):
        # 再読み込み数設定用Enum
        SMALL = 12
        STANDARD = 24
        LARGE = 36

    def get(self, request):
        # ajaxリクエストか否か判定
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            article_start_index = int(request.GET.get('index')) * self.LoadNum.SMALL + 1
            article_end_index = article_start_index + self.LoadNum.SMALL
            article_object_list = list(ConsultWindow.objects.order_by('-created_at')[article_start_index:article_end_index])

            load_article = {
                'discover_article' : self.create_consult_window_list(article_object_list),
            }

            return render(request, 'sharetech/async_load_template.html', load_article)

        # 直接GETリクエストが来た場合はトップページにリダイレクト
        return edirect('top')

async_consult_window_load = AsyncArticleLoadView.as_view()