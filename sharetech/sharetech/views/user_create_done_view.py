from django.views import generic
from sharetech.constants.messages import GeneralMessages

class UserCreateDoneView(generic.TemplateView):

    template_name = 'sharetech/register_done.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['message'] = GeneralMessages().pre_register
        return context

user_create_done = UserCreateDoneView.as_view()