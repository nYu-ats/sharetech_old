from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import (
    _unicode_ci_compare, UserModel,
)
from sharetech.validators.custom_validator import email_validate

class PasswordResetForm(PasswordResetForm):
    # override
    email = forms.EmailField(
        label = '',
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder':'Email', 'autocomplete': 'email'})
    )
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # エラーメッセージ変更のため、defaultのvalidatorを上書き
        self.fields['email'].validators = [email_validate]

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
