from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.html import format_html, format_html_join
from django.utils.functional import lazy

class SetPasswordForm(SetPasswordForm):
    # override
    def _password_validators_help_text_html(password_validators=None):
        """
        Return an HTML string with all help texts of all configured validators
        in an <ul>.
        """
        help_texts = [
            'パスワードを他の個人情報と類似させないでください。',
            '8文字以上である必要があります。',
            '一般的に使用される言葉をパスワードにすることはできません。',
            'すべて数値にすることはできません。'
        ]
        help_items = format_html_join('', '<li>{}</li>', ((help_text,) for help_text in help_texts))
        return format_html('<ul>{}</ul>', help_items) if help_items else ''

    password_validators_help_text_html = lazy(_password_validators_help_text_html, str)

    error_messages = {
        'password_mismatch': 'パスワードが一致しませんでした',
    }
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder':'New password', 'autocomplete': 'new-password'}),
        strip=False,
        # help_text=password_validation.password_validators_help_text_html(),
        help_text=password_validators_help_text_html,
    )
    new_password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder':'New password confirmation', 'autocomplete': 'new-password'}),
    )
