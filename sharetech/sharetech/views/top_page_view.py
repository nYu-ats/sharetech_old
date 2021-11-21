from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.utils.model_template_adapter import ConsultWindodwAdapter
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from enum import IntEnum

User = get_user_model()

class TopPageView(LoginRequiredMixin, View):

    class DisplayNum(IntEnum):
        # 各抽出記事抽出数設定用Enum
        SMALL = 12
        STANDARD = 24
        LARGE = 30

    template_name = 'sharetech/top.html'

    def get(self, request, *args, **kwargs):
        selected_obj_array = list()
        
        # 一度取得した相談窓口は、重複して画面に初期表示しないようにする
        # 記事抽出の優先度は、注目->おすすめ->新着->発見
        # TODO 注目、おすすめ、発見については、フィルタ条件要検討
        # 注目窓口抽出
        attention_consult_window_object_list = list(ConsultWindow.objects.order_by('-viewed_num')[:self.DisplayNum.STANDARD])
        selected_obj_array.extend([int(consult_window_obj.id) for consult_window_obj in attention_consult_window_object_list])

        # おすすめ窓口抽出
        reccomend_consult_window_object_list = list(ConsultWindow.objects.exclude(pk__in=selected_obj_array).order_by('-applyed_num')[:self.DisplayNum.STANDARD])
        selected_obj_array.extend([int(consult_window_obj.id) for consult_window_obj in reccomend_consult_window_object_list])

        # 新着窓口抽出
        latest_consult_window_object_list = list(ConsultWindow.objects.exclude(pk__in=selected_obj_array).order_by('created_at')[:self.DisplayNum.SMALL])
        selected_obj_array.extend([int(consult_window_obj.id) for consult_window_obj in latest_consult_window_object_list])

        # 発見窓口抽出
        discover_consult_window_object_list = list(ConsultWindow.objects.exclude(pk__in=selected_obj_array).order_by('-viewed_num')[:self.DisplayNum.LARGE])
        
        selected_article_list = {
            'latest_article' : ConsultWindodwAdapter(latest_consult_window_object_list).convert_to_template_context(),
            'attention_article' : ConsultWindodwAdapter(attention_consult_window_object_list).convert_to_template_context(),
            'discover_article' : ConsultWindodwAdapter(discover_consult_window_object_list).convert_to_template_context(),
            'reccomend_article' : ConsultWindodwAdapter(reccomend_consult_window_object_list).convert_to_template_context(),
            }

        return render(request, 'sharetech/top.html', selected_article_list)
    pass

top_page = TopPageView.as_view()
