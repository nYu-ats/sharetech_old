from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from .base_page_common_view import BasePageCommonView
from sharetech.constants import ImageConstants, Constants
from sharetech.models.user_specialize import UserSpecialize

class ProfileView(BasePageCommonView):
    '''
    プロファイル
    '''
    def get(self, request, *args, **kwargs):
        self._template = 'sharetech/mypage.html'

        user_id = self.request.user
        user_info = CustomUser.objects.get(email=user_id)
        apply_history_list = list(ConsultApply.objects.filter(user_id = user_info.id, is_deleted = False))
        # 重複をなくすため一旦set変換
        applyed_consult_window_set = {model.consult_window_id for model in apply_history_list}

        create_consult_window = list(ConsultWindow.objects.filter(expert_user_id = user_info.id, is_deleted = False))
        specialize_list = list(UserSpecialize.objects.filter(user_id=user_info.id))

        self.prepare().set_category_dict().update(
            {
                'user_info': user_info,
                'icon_img': ImageConstants.get_user_icon_path() + user_info.icon_path.name if user_info.icon_path.name != '' else ImageConstants.get_default_icon_path(),
                'applyed_consult_window': self.create_consult_window_list(list(applyed_consult_window_set)),
                'create_consult_window': self.create_consult_window_list(create_consult_window),
                'specialize': specialize_list,
            }
        )

        return render(request, self._template, self._base_context_dict)

profile = ProfileView.as_view()
