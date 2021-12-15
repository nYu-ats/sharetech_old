from django.shortcuts import render
from django.views import View
from .base_page_common_view import BasePageCommonView
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_consult_window_mapping import CategoryConsultWindowMapping
from enum import IntEnum
from sharetech.constants import ImageConstants, Constants

class ConsultWindowDetailView(BasePageCommonView):
    '''
    相談窓口詳細
    '''
    class UserCheck(IntEnum):
        # 記事詳細ページにアクセスしてきたユーザーの判別に使用
        other_user = 0
        create_user = 1
        applying_user = 2

    def get(self, request, *args, **kwargs):
        login_user = self.request.user
        # デフォルトのログインユーザーの種別として相談窓口作成者以外をセットする
        login_user_flg = self.UserCheck.other_user
        consult_window_id = kwargs.get('consult_window_id')

        # ログインユーザーと相談窓口の関連の確認
        # TODO apply_status enum化
        if len(list(CustomUser.objects.filter(email=login_user))) > 0:
            login_user_flg = self.UserCheck.create_user
        elif len(list(ConsultApply.objects.filter(user_id = login_user).filter(apply_status__in=[0, 3]))) > 0:
            login_user_flg = self.UserCheck.applying_user

        # 相談窓口詳細取得
        consult_window_detail = ConsultWindow.objects.get(id = consult_window_id)

        # 対象記事に付与されているカテゴリ一覧を取得
        category_list = [category.category_id.category_name for category in list(
                CategoryConsultWindowMapping.objects.filter(consult_window_id = consult_window_id)
                )]

        self.prepare().set_category_dict().update(
            {
                'login_user_flg' : login_user_flg,
                'title' : consult_window_detail.consult_window_title,
                'overview' : consult_window_detail.consult_window_overview,
                'applyed_num' : consult_window_detail.applyed_num,
                'created_at' : consult_window_detail.created_at,
                'archivement' : consult_window_detail.archivement,
                'expert_user_id' : consult_window_detail.expert_user_id.id,
                'icon_path' : Constants.get_image_path() + consult_window_detail.expert_user_id.icon_path if consult_window_detail.expert_user_id.icon_path != None else ImageConstants.get_default_icon_path(),
                'company' : consult_window_detail.expert_user_id.company,
                'username' : consult_window_detail.expert_user_id.username,
                'occupation' : consult_window_detail.expert_user_id.occupation_id.name,
                'introduction' : consult_window_detail.expert_user_id.introduction,
                'categories' : category_list,
            }
        )

        # TODO スーパークラスの作りそどうするか、topとの棲み分けを考える必要あり
        return render(request, 'sharetech/consult_window_detail.html', self._base_context_dict)

consult_window_detail = ConsultWindowDetailView.as_view()