from django.core.signing import BadSignature, SignatureExpired, loads
from django.http.response import HttpResponseBadRequest
from django.views import generic
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
import time

User = get_user_model()

class EmailChangeComplete(generic.TemplateView):

    template_name = 'sharetech/email_chnage_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS')

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age = self.timeout_seconds)
        except SignatureExpired:
            # url有効期限切れ
            return HttpResponseBadRequest()
        except BadSignature:
            # token誤り
            return HttpResponseBadRequest()
        else:
            # tokenは問題なし
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if user.tmp_email is not None:
                    user.email = user.tmp_email
                    user.tmp_email = None
                    user.email_verified_at = time.strftime('%Y-%m-%d %H:%M:%S')
                    user.save()
                    return redirect('login')
        
        return HttpResponseBadRequest()

email_change_complete = EmailChangeComplete.as_view()