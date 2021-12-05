from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from sharetech.constants import Constants
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.utils.model_template_adapter import CategoryAdapter
from sharetech.models.category_mst import CategoryMst
from enum import IntEnum

User = get_user_model()

class BasePageCommonView(LoginRequiredMixin, View):
    '''
    共通的に利用される処理
    '''

    # 各抽出記事抽出数設定用Enum
    class DisplayNum(IntEnum):
        SMALL = 12
        STANDARD = 24
        LARGE = 36
        
    DEFAULT_USER_ICON_PATH = 'default_avater.png'
    _template = 'sharetech/top.html'
    # templateへ渡す相談窓口dict
    _selected_article_dict = {}

    # templateへ渡すパラメータにカテゴリデータをセット
    def set_category_dict(self):
        # dict初期化
        self._selected_article_dict.clear()
        category_dict = {}
        
        category_list = list(CategoryMst.objects.filter(category_hierarchy=2).order_by('category_hierarchy'))
        big_cat_set = {big_cat.parent_category_id.category_name for big_cat in category_list}
        for big_cat in sorted(big_cat_set):
            category_dict[big_cat] = [
                (category.id, category.category_name) for category in category_list 
                            if category.parent_category_id.category_name == big_cat
                            ]

        self._selected_article_dict.update(
                {
                'category_dict' : category_dict
                }
            )

        return self._selected_article_dict

    def create_consult_window_list(self, consult_window_models):
        consult_window_list = []

        for _, consult_window_model in enumerate(consult_window_models):
            consult_window_content = {
                'number' : str(consult_window_model.id),
                'expert_icon_path' : Constants.get_image_path() + consult_window_model.expert_user_id.icon_path if consult_window_model.expert_user_id.icon_path != None else Constants.get_image_path() + self.DEFAULT_USER_ICON_PATH,
                'created_at' : consult_window_model.created_at,
                'title' : consult_window_model.consult_window_title,
                'applyed_num' : consult_window_model.applyed_num,
                'expert_name' : consult_window_model.expert_user_id.family_name_jp + consult_window_model.expert_user_id.first_name_jp,
                'expert_companey' : consult_window_model.expert_user_id.company,
                }
            consult_window_list.append(consult_window_content)
        
        return consult_window_list


    # templateへ渡すパラメータにログインユーザー情報をセット
    # def set_login_user_info_dict():

