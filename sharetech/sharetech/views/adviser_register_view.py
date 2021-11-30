from django.views import generic
from django.contrib.auth import get_user_model
from ..forms.adviser_register_form import AdviserRegisterForm

# ユーザーモデル(カスタム)取得
User = get_user_model()

class AdviserRegisterView(generic.TemplateView):

    # 専門家登録窓口フォーム
    adviser_register_form = AdviserRegisterForm
    template_name = 'sharetech/adviser_register.html'

adiviser_register = AdviserRegisterView.as_view()