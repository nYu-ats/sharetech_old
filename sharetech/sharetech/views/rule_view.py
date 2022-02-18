from .base_page_common_view import BasePageCommonView
from django.shortcuts import render
from sharetech.models.user import CustomUser
from sharetech.constants import ImageConstants, Constants

class RuleView(BasePageCommonView):
    '''
    利用規約
    '''

    def get(self, request, *args, **kwargs):
        self._template = 'sharetech/rule.html'
        user_id = self.request.user
        user_info = CustomUser.objects.get(email=user_id)

        self.prepare().set_category_dict().update(
            {
                'user_info': user_info,
                'icon_img': ImageConstants.get_user_icon_path() + user_info.icon_path.name if user_info.icon_path.name != '' else ImageConstants.get_default_icon_path(),
            }
        )
        return render(request, self._template, self._base_context_dict)

rule = RuleView.as_view()