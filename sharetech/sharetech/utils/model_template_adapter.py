from abc import ABC, abstractmethod
from sharetech.models import *
from sharetech.constants import Constants

class BaseModelTemplateAdapter(ABC):
    '''
    DB抽出データをtemplateに渡せる形に変換するための抽象クラス
    '''
    
    @abstractmethod
    def convert_to_template_context(self):
        pass

class ConsultWindodwAdapter(BaseModelTemplateAdapter):
    '''
    DB抽出データをtemplateで展開できる形に変換する
    '''
    DEFAULT_USER_ICON_PATH = 'default_avater.png'

    def __init__(self, consult_window_models: ConsultWindow):
        self.__consult_window_models = consult_window_models
    
    def convert_to_template_context(self):
        consult_window_list = []

        for index, consult_window_model in enumerate(self.__consult_window_models):
            consult_window_content = {
                'number' : str(index + 1),
                'expert_icon_path' : Constants.get_image_path() + consult_window_model.expert_user_id.icon_path if consult_window_model.expert_user_id.icon_path != None else Constants.get_image_path() + self.DEFAULT_USER_ICON_PATH,
                'created_at' : consult_window_model.created_at,
                'title' : consult_window_model.consult_window_title,
                'applyed_num' : consult_window_model.applyed_num,
                'expert_name' : consult_window_model.expert_user_id.family_name_jp + consult_window_model.expert_user_id.first_name_jp,
                'expert_companey' : consult_window_model.expert_user_id.company,
                }
            consult_window_list.append(consult_window_content)
        
        return consult_window_list
            