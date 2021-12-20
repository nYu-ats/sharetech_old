from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from sharetech.constants import Constants
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.models.category_mst import CategoryMst
from sharetech.models.consult_apply import ConsultApply
from enum import IntEnum
from sharetech.constants import ImageConstants

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
        
    _template = 'sharetech/top.html'
    # templateへ渡す相談窓口dict
    _base_context_dict = {}

    # ログイン状態の場合の共通表示制御
    def prepare(self):
        # ログインユーザー情報取得
        self._base_context_dict.clear()
        login_user = self.request.user
        login_user_id = User.objects.get(email = login_user)
        self._base_context_dict.update(
            {
                'login_user_icon': ImageConstants.get_user_icon_path() + login_user_id.icon_path.name if login_user_id.icon_path.name != '' else ImageConstants.get_default_icon_path(),
            }
        )
        # 申込中の相談があるか否か判定
        self.__set_apply_status(login_user_id)

        return self

    # templateへ渡すパラメータにカテゴリデータをセット
    def set_category_dict(self):
        # すでにカテゴリ取得済みの場合は処理をスキップ
        if 'category_dict' in self._base_context_dict:
            return self._base_context_dict

        category_dict = {}
        
        category_list = list(CategoryMst.objects.filter(category_hierarchy=2).order_by('category_hierarchy'))
        big_cat_set = {big_cat.parent_category_id.category_name for big_cat in category_list}
        for big_cat in sorted(big_cat_set):
            category_dict[big_cat] = [
                (category.id, category.category_name) for category in category_list 
                            if category.parent_category_id.category_name == big_cat
                            ]

        self._base_context_dict.update(
                {
                'category_dict' : category_dict
                }
            )

        return self._base_context_dict

    def create_consult_window_list(self, consult_window_models):
        consult_window_list = []

        for _, consult_window_model in enumerate(consult_window_models):
            consult_window_content = {
                'number' : str(consult_window_model.id),
                'expert_icon_path' : ImageConstants.get_user_icon_path() + consult_window_model.expert_user_id.icon_path.name if consult_window_model.expert_user_id.icon_path.name != None else ImageConstants.get_default_icon_path(),
                'created_at' : consult_window_model.created_at,
                'title' : consult_window_model.consult_window_title,
                'applyed_num' : consult_window_model.applyed_num,
                'expert_name' : consult_window_model.expert_user_id.family_name_jp + consult_window_model.expert_user_id.first_name_jp,
                'expert_companey' : consult_window_model.expert_user_id.company,
                }
            consult_window_list.append(consult_window_content)
        
        return consult_window_list

    # 申込中の相談があるか否か判定
    def __set_apply_status(self, login_user_id):
        # TODO 申込ステータスEnum定義
        # TODO 複数申込中があった場合の対応(templateと合わせて対応の必要あり)
        # TODO 申込済みについても、画面制御が必要
        applying = list(ConsultApply.objects.filter(user_id = login_user_id, apply_status = 1))
        if len(applying) > 0:
            applying_flg = str(1)
            consult_window_id = applying[0].consult_window_id.id
            applying_title = applying[0].consult_window_id.consult_window_title
        else:
            applying_flg = str(0)
            consult_window_id = ''
            applying_title = ''

        self._base_context_dict.update({
            'applying_flg': applying_flg,
            'consult_window_id': consult_window_id,
            'applying_title': applying_title,
        })

