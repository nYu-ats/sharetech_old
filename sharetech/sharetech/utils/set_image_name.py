from django.conf import settings
from datetime import date
import os

class SetImageName:
    '''
    画像ファイル名をセットする
    '''
    @staticmethod
    def set_icon_name(model, filename):
        '''
        アイコン画像パスフォーマット
        <user id>/icon_<user_id>_<today[date]>.<extension>
        '''
        extension = os.path.splitext(filename)[1]
        return str(model.id) + '/icon_' + str(model.id) + '_' + str(date.today()).replace('-', '_') + extension