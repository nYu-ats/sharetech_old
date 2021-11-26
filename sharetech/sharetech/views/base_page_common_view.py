from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.utils.model_template_adapter import CategoryAdapter
from sharetech.models.category_mst import CategoryMst
from enum import IntEnum

User = get_user_model()

class BasePageCommonView(LoginRequiredMixin, View):
    '''
    トップページ表示の共通処理
    '''

    # 各抽出記事抽出数設定用Enum
    class DisplayNum(IntEnum):
        SMALL = 12
        STANDARD = 24
        LARGE = 36
    
    _template = 'sharetech/top.html'

    # templateへ渡すdict
    _selected_article_dict = {}

    # templateへ渡すパラメータにカテゴリデータをセット
    def set_category_dict(self):
        # dict初期化
        self._selected_article_dict.clear()
        
        category_list = list(CategoryMst.objects.filter(category_hierarchy=2).order_by('category_hierarchy'))
        self._selected_article_dict.update(
                {
                'category_dict' : CategoryAdapter.convert_to_template_context(category_list)
                }
            )

        return self._selected_article_dict

    # templateへ渡すパラメータにログインユーザー情報をセット
    # def set_login_user_info_dict():

