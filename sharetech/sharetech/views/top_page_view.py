from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from .base_page_common_view import BasePageCommonView

class TopPageView(BasePageCommonView):
    '''
    デフォルトトップページ
    '''

    def get(self, request, *args, **kwargs):  

        # 一度取得した相談窓口は、重複して画面に初期表示しないようにする
        # 記事抽出の優先度は、注目->おすすめ->新着->発見
        selected_obj_array = list()    

        # TODO 注目、おすすめ、発見については、フィルタ条件要検討
        # TODO 記事取得のクエリ1本にまとめて(all)ロジック部分で記事の切り出ししたほうがいいかも？
        # 注目窓口抽出
        attention_consult_window_object_list = list(ConsultWindow.objects.filter(is_deleted = False).order_by('-viewed_num')[:self.DisplayNum.SMALL])
        selected_obj_array.extend([int(consult_window_obj.id) for consult_window_obj in attention_consult_window_object_list])

        # おすすめ窓口抽出
        reccomend_consult_window_object_list = list(ConsultWindow.objects.filter(is_deleted = False).exclude(
            pk__in=selected_obj_array).order_by('-applyed_num')[:self.DisplayNum.SMALL])
        selected_obj_array.extend([int(consult_window_obj.id) for consult_window_obj in reccomend_consult_window_object_list])

        # 新着窓口抽出
        latest_consult_window_object_list = list(ConsultWindow.objects.filter(is_deleted = False).exclude(
            pk__in=selected_obj_array).order_by('created_at')[:self.DisplayNum.SMALL])
        selected_obj_array.extend([int(consult_window_obj.id) for consult_window_obj in latest_consult_window_object_list])

        # 発見窓口抽出
        discover_consult_window_object_list = list(ConsultWindow.objects.filter(is_deleted = False).exclude(
            pk__in=selected_obj_array).order_by('-viewed_num')[:self.DisplayNum.SMALL])
        
        self.prepare().set_category_dict().update(
            {
            'latest_article' : self.create_consult_window_list(latest_consult_window_object_list),
            'attention_article' : self.create_consult_window_list(attention_consult_window_object_list),
            'discover_article' : self.create_consult_window_list(discover_consult_window_object_list),
            'reccomend_article' : self.create_consult_window_list(reccomend_consult_window_object_list),
            }
        )

        return render(request, self._template, self._base_context_dict)

top_page = TopPageView.as_view()
