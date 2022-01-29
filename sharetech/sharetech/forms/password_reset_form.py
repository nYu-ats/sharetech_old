from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import (
    _unicode_ci_compare, UserModel,
)

class PasswordResetForm(PasswordResetForm):
    # override
    def get_users(self, email):
        """
        is_active field を使用しないようにオーバーライド
        """
        email_field_name = UserModel.get_email_field_name()
        active_users = UserModel._default_manager.filter(**{
            '%s__iexact' % email_field_name: email,
        })
        return (
            u for u in active_users
            if u.has_usable_password() and
            _unicode_ci_compare(email, getattr(u, email_field_name))
        )
