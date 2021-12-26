from django.contrib.auth.backends import ModelBackend
from sharetech.models.user import CustomUser

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.exclude(email_verified_at = None).get(email=email)
        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user