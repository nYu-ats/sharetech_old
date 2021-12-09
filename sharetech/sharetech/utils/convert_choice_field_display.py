from django.forms import ModelChoiceField

class ConvertChoiceFieldDisplay(ModelChoiceField):
    '''
    外部参照選択フィールドオブジェクトの画面表示文字列を変更
    '''

    def label_from_instance(self, choice_obj):
        return choice_obj.name