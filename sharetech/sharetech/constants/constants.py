class Constants:
    # アプリケーション内での固定値を保持する

    # ローカル環境での記事画像データ保存先
    PROJECT_URL = '/sharetech/'
    IMG_DIR = 'img/'

    @classmethod
    def get_static_file_path(self):
        return '..' + self.PROJECT_URL

    @classmethod
    def get_image_path(self):
        image_path = self.PROJECT_URL + self.IMG_DIR
        return image_path