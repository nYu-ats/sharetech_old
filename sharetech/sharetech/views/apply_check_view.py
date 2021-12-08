from django.shortcuts import render
from django.views import View
from .base_page_common_view import BasePageCommonView
from django.http.response import JsonResponse
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply
from sharetech.models.consult_window import ConsultWindow

class ApplyCheckView(BasePageCommonView):
    '''
    申込申請
    '''
    def get(self, request, *args, **kwargs):
        apply_result = ConsultApply.objects.create(
            consult_window_id = ConsultWindow.objects.get(id = kwargs['consult_window_id']),
            user_id = CustomUser.objects.get(email = self.request.user),
            apply_status = 1,
        )
        return JsonResponse({"result" : apply_result.id})

apply_check = ApplyCheckView.as_view()