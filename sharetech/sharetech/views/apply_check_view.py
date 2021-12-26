from django.shortcuts import render
from .base_page_common_view import BasePageCommonView
from django.http.response import JsonResponse
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from sharetech.models.consult_window import ConsultWindow

class ApplyCheckView(BasePageCommonView):
    '''
    申込申請
    '''

    # TODO ここPOSTで受けなきゃ、、
    def get(self, request, *args, **kwargs):
        # ajaxリクエストか否か判定
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            apply_result = ConsultApply.objects.create(
                consult_window_id = ConsultWindow.objects.get(id = kwargs['consult_window_id']),
                user_id = CustomUser.objects.get(email = self.request.user),
                apply_status = 1,
            )
            return JsonResponse({"result" : apply_result.id})

        # 直接GETリクエストが来た場合はトップページにリダイレクト
        return edirect('top')

apply_check = ApplyCheckView.as_view()