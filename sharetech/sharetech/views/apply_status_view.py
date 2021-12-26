from django.shortcuts import render
import json
from .base_page_common_view import BasePageCommonView
from django.http.response import JsonResponse
from sharetech.models.user import CustomUser
from sharetech.models.consult_apply import ConsultApply

class ApplyStatusView(BasePageCommonView):
    '''
    申込状況の確認
    '''

    def post(self, request, *args, **kwargs):
        # ajaxリクエストか否か判定
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            apply_data = json.loads(request.body)
            # 申込履歴の存在チェック
            consult_apply = ConsultApply.objects.get(
                consult_window_id = int(apply_data.get('windowId')),
                user_id = CustomUser.objects.get(email = self.request.user).id,
                apply_status = 1,
                )
            # 申込ステータス更新
            consult_apply.apply_status = int(apply_data.get('applyStatus'))
            consult_apply.save()

            return JsonResponse({'result': 'success'})
            
        # 直接GETリクエストが来た場合はトップページにリダイレクト
        return edirect('top')

apply_status = ApplyStatusView.as_view()