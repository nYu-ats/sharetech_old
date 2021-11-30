from abc import ABC, abstractmethod
from sharetech.models import *
from sharetech.constants import Constants
from django.db import models

class BaseModelTemplateAdapter(ABC):
    '''
    DB抽出データをtemplateに渡せる形に変換するための抽象クラス
    '''
    
    @abstractmethod
    def convert_to_template_context(self):
        pass

class ConsultWindodwAdapter(BaseModelTemplateAdapter):
    '''
    DB抽出データをtemplateで展開しやすい形に変換
    '''
    DEFAULT_USER_ICON_PATH = 'default_avater.png'

    @classmethod
    def convert_to_template_context(cls, consult_window_models):
        consult_window_list = []

        for _, consult_window_model in enumerate(consult_window_models):
            consult_window_content = {
                'number' : str(consult_window_model.id),
                'expert_icon_path' : Constants.get_image_path() + consult_window_model.expert_user_id.icon_path if consult_window_model.expert_user_id.icon_path != None else Constants.get_image_path() + cls.DEFAULT_USER_ICON_PATH,
                'created_at' : consult_window_model.created_at,
                'title' : consult_window_model.consult_window_title,
                'applyed_num' : consult_window_model.applyed_num,
                'expert_name' : consult_window_model.expert_user_id.family_name_jp + consult_window_model.expert_user_id.first_name_jp,
                'expert_companey' : consult_window_model.expert_user_id.company,
                }
            consult_window_list.append(consult_window_content)
        
        return consult_window_list

class CategoryAdapter(BaseModelTemplateAdapter):
    '''
    DB抽出データをtemplateで展開しやすい形に変換
    '''
    @classmethod
    def convert_to_template_context(cls, category_models):
        category_dict = {}
        big_cat_set = {big_cat.parent_category_id.category_name for big_cat in category_models}

        for big_cat in sorted(big_cat_set):
            category_dict[big_cat] = [(category.id, category.category_name) for category in category_models 
                            if category.parent_category_id.category_name == big_cat]

        return category_dict
        