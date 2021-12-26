import os

class Constants:
    # アプリケーション内での固定値を保持する

    # ローカル環境での記事画像データ保存先
    PROJECT_URL = '/sharetech'
    IMG_DIR = '/'

    @classmethod
    def get_static_file_path(cls):
        return '..' + cls.PROJECT_URL

    @classmethod
    def get_image_path(cls):
        image_path = cls.PROJECT_URL + cls.IMG_DIR
        return image_path

class ImageConstants(Constants):
    '''
    画像関連固定値
    '''

    DEFAULT_USER_ICON_PATH = 'img/default_avater.png'
    USER_ICON_ROOT_PATH = 'media/'

    @classmethod
    def get_default_icon_path(cls):
        return 'sharetech/' + cls.DEFAULT_USER_ICON_PATH

    @classmethod
    def get_user_icon_path(cls):
        return cls.USER_ICON_ROOT_PATH
