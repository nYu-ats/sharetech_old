from django.core.validators import EmailValidator
from sharetech.constants.messages import ErrorMessage, RePatterns

class CustomEmailValidator(EmailValidator):
    # メールアドレスvalidator
    def __init__(self, **kwargs):
        # エラーメッセージ上書き
        super().__init__(message=ErrorMessage().failuer_mail_format, **kwargs)

email_validate = CustomEmailValidator()