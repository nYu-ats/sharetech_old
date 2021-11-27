from django.views import generic
from django.contrib.auth import get_user_model
from ..forms.adviser_register_form import AdviserRegisterForm

# ユーザーモデル(カスタム)取得
User = get_user_model()

class AdviserRegisterView(generic.CreateView):

    # 専門家登録窓口フォーム
    form_class = AdviserRegisterForm
    template_name = 'sharetech/adviser_register.html'

    def form_valid(self, form):
        user = form.save(commit=False)

adiviser_register = AdviserRegisterView.as_view()