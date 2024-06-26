class GeneralMessages:

    __PRE_REGISTER = "仮登録が完了しました。\n\
    ご入力いただいたメールアドレス宛に登録完了用のURLを送信しましたので、\n\
    メールをご確認いただき、添付のURLへアクセスして登録を完了させてください。"

    __CHANGE_EMAIL = "メールアドレスの変更を受付ました。\n\
    ご入力いただいた新しいメールアドレス宛に変更完了用のURLを送信しましたので、\n\
    メールをご確認いただき、添付のURLへアクセスして変更を完了させてください。"

    __CHANGE_PASSWORD = "パスワードの変更をしました。\n\
    新しいパスワードで再度ログインしてください。"

    __REREGISTER_PASSWORD = "パスワードの再設定を受け付けました。\n\
    ご登録のメールアドレス宛に変更完了用のURLを送信しましたので、\n\
    メールをご確認いただき、添付のURLへアクセスして変更を完了させてください。"

    @property
    def pre_register(self):
        return self.__PRE_REGISTER

    @property
    def change_email(self):
        return self.__CHANGE_EMAIL
    
    @property
    def change_password(self):
        return self.__CHANGE_PASSWORD

    @property
    def reregister_password(self):
        return self.__REREGISTER_PASSWORD

class ErrorMessage:

    __FAILURE_LOGIN_AUTH = "パスワードもしくはメールアドレスが誤っています"

    __FAILURE_NAME_KANA = "氏名(カナ)は全角カタカナで入力してください"

    __FAILURE_NAME_ROMA = "氏名(ローマ字)は半角英字で入力してください"

    __FAILURE_PASSWORD_LENGTH = "パスワードは8文字以上20文字以内で設定してください"

    __FAILURE_PASSWORD_FORMAT = "パスワードは半角英字と数字で設定してください"

    __FAILURE_PASSWORD_MATCH = "確認用パスワードが一致しません"

    __FAILURE_MAIL_FORMAT = "メールアドレスの形式が誤っています"

    __FAILURE_USER_NOT_EXIST = "メールアドレスの形式が誤っています"

    __FAILURE_CURRENT_PASSWORD_NOT_EXIST = "現在のパスワードが一致しません"

    __FAILURE_EMAIL_MATCH = "確認用メールアドレスが一致しません"

    __FAILURE_SCHEDULER_URL_PATTERN = "スケジューラー調整URLが不正な値です"

    @property
    def failuer_login_auth(self):
        return self.__FAILURE_LOGIN_AUTH

    @property
    def failuer_name_kana(self):
        return self.__FAILURE_NAME_KANA

    @property
    def failuer_name_roma(self):
        return self.__FAILURE_NAME_ROMA

    @property
    def failuer_password_length(self):
        return self.__FAILURE_PASSWORD_LENGTH

    @property
    def failuer_password_format(self):
        return self.__FAILURE_PASSWORD_FORMAT

    @property
    def failuer_password_match(self):
        return self.__FAILURE_PASSWORD_MATCH

    @property
    def failuer_mail_format(self):
        return self.__FAILURE_MAIL_FORMAT

    @property
    def failuer_user_not_exist(self):
        return self.__FAILURE_USER_NOT_EXIST

    @property
    def failuer_current_password_not_exist(self):
        return self.__FAILURE_CURRENT_PASSWORD_NOT_EXIST

    @property
    def failuer_email_match(self):
        return self.__FAILURE_EMAIL_MATCH

    @property
    def failuer_scheduler_url_pattern(self):
        return self.__FAILURE_SCHEDULER_URL_PATTERN

class RePatterns:

    __EMAIL_PATTERN = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    __PASSWORD_PATTERN = '\A(?=.*?[a-z])(?=.*?\d)[a-z\d]{8,20}\Z(?i)'

    __KANA_PATTERN = '[\u30A1-\u30F4]+'
    
    __ROMA_PATTERN = '^[a-zA-Z]+$'

    __SCHEDULER_URL_PATTERN = "https?://[\w!?/+\-_~;.,*&@#$%()'[\]]+"

    @property
    def email_pattern(self):
        return self.__EMAIL_PATTERN

    @property
    def password_pattern(self):
        return self.__PASSWORD_PATTERN

    @property
    def kana_pattern(self):
        return self.__KANA_PATTERN

    @property
    def roma_pattern(self):
        return self.__ROMA_PATTERN

    @property
    def scheduler_url_pattern(self):
        return self.__SCHEDULER_URL_PATTERN