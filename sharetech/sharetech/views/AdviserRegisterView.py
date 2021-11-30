from django.views import generic
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from ..forms.adviser_register_form import AdviserRegisterForm
from sharetech.utils.model_template_adapter import ConsultWindodwAdapter
from sharetech.models import *

# ユーザーモデル(カスタム)取得
User = get_user_model()

class AdviserRegisterView(LoginRequiredMixin, View):

    # 専門家登録窓口フォーム
    template_name = 'sharetech/adviser_register.html'
    form_class = AdviserRegisterForm
    model = ConsultWindow

    def get(self, request, *args, **kwargs):
        params = {'form': AdviserRegisterForm()}
        return render(request, 'sharetech/adviser_register.html', params)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print(self.request.user)
        return render(request, 'sharetech/adviser_register.html')

    def form_valid(self, form):
        print(self.request.user)
        return super().form_valid(form)

adiviser_register = AdviserRegisterView.as_view()