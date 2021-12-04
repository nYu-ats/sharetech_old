from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from ..forms.adviser_register_form import AdviserRegisterForm
from sharetech.utils.model_template_adapter import *
from sharetech.models import *

# ユーザーモデル(カスタム)取得
User = get_user_model()

class AdviserRegisterView(LoginRequiredMixin, View):

    # 専門家登録窓口フォーム
    template_name = 'sharetech/adviser_register.html'
    params = {}

    def get(self, request, *args, **kwargs):
        self.params.clear()
        category_list = list(CategoryMst.objects.order_by('id'))
        self.params.update(
                {
                'form': AdviserRegisterForm(),
                'category_dict' : CategoryAdapter.convert_to_template_context(category_list),
                }
            )
        return render(request, 'sharetech/adviser_register.html', self.params)

    def post(self, request, *args, **kwargs):
        # 相談窓口を登録
        consultWindow = ConsultWindow(
            expert_user_id = CustomUser.objects.get(id=self.request.user.id),
            consult_window_title = self.request.POST.get("consult_window_title"),
            consult_window_overview = self.request.POST.get("consult_window_overview"),
            consult_price = self.request.POST.get("consult_price"),
            archivement = self.request.POST.get("archivement")
        )
        consultWindow.save()
        # カテゴリと相談窓口のマッピングを登録
        for cat_id in self.request.POST.getlist("cat"):
            CategoryConsultWindowMapping.objects.create(
                category_id = CategoryMst.objects.get(id=cat_id),
                consult_window_id = consultWindow
            )
        return render(request, 'sharetech/adviser_register.html', self.params)

adiviser_register = AdviserRegisterView.as_view()