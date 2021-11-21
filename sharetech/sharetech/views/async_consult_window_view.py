from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.utils.model_template_adapter import ConsultWindodwAdapter
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from enum import IntEnum

class AsyncArticleLoadView(LoginRequiredMixin, View):
    class LoadNum(IntEnum):
        # 再読み込み数設定用Enum
        SMALL = 10
        STANDARD = 20
        LARGE = 30

    def get(self, request):
        if(request.is_ajax()):
            article_start_index = int(request.GET.get('index')) * self.LoadNum.STANDARD + 1
            article_end_index = article_start_index + self.LoadNum.STANDARD
            article_object_list = list(ConsultWindow.objects.order_by('-created_at')[article_start_index:article_end_index])

            load_article = {
                'reccomend_article' : ConsultWindodwAdapter(article_object_list).convert_to_template_context(),
            }

            return render(request, 'sharetech/additional_article.html', load_article)
    pass

async_article_load = AsyncArticleLoadView.as_view()