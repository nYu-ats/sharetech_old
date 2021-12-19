from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from enum import IntEnum

class AsyncArticleLoadView(LoginRequiredMixin, View):
    class LoadNum(IntEnum):
        # 再読み込み数設定用Enum
        SMALL = 12
        STANDARD = 24
        LARGE = 36

    def get(self, request):
        if(request.is_ajax()):
            article_start_index = int(request.GET.get('index')) * self.LoadNum.SMALL + 1
            article_end_index = article_start_index + self.LoadNum.SMALL
            article_object_list = list(ConsultWindow.objects.order_by('-created_at')[article_start_index:article_end_index])

            load_article = {
                'discover_article' : ConsultWindodwAdapter.convert_to_template_context(article_object_list),
            }

            return render(request, 'sharetech/async_load_template.html', load_article)
    pass

async_consult_window_load = AsyncArticleLoadView.as_view()