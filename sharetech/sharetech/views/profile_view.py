from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from sharetech.utils.model_template_adapter import ConsultWindodwAdapter
from django.http.response import JsonResponse
from sharetech.models.consult_window import ConsultWindow
from sharetech.models.category_mst import CategoryMst
from .base_page_common_view import BasePageCommonView

class ProfileView(BasePageCommonView):
    '''
    プロファイル
    '''
    def get(self, request, *args, **kwargs):
        return render(request, 'sharetech/mypage.html')

profile = ProfileView.as_view()
