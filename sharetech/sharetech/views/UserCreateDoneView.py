from django.views import generic
from django.contrib.auth import get_user_model

# ユーザーモデル(カスタム)取得
User = get_user_model()

class UserCreateDoneView(generic.TemplateView):

    template_name = 'sharetech/register_done.html'

user_create_done = UserCreateDoneView.as_view()