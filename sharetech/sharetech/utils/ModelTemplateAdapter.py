from abc import ABC, abstractmethod
from sharetech.models import *

class ModelTemplateAdapter(ABC):
    
    @abstractmethod
    def convert_to_template_context(self):
        pass

class ArticleAdapter(ModelTemplateAdapter):
    DEFAULT_USER_ICON_PATH = 'default_icon.png'
    DEFAULT_USER_COMPANY_NAME = ''

    def __init__(self, article_models: Article):
        self.__article_models = article_models
    
    def convert_to_template_context(self):
        article_list = []

        for index, article_model in enumerate(self.__article_models):
            article_content = {
                'number' : str(index + 1),
                'eyecatch_path' : article_model.eyecatch_path,
                'created_at' : article_model.created_at,
                'title' : article_model.title,
                'favorite_num' : article_model.favorite_count,
                'contributor_icon_path' : article_model.contributor_id.icon_path if article_model.contributor_id.icon_path != None else self.DEFAULT_USER_ICON_PATH,
                'contributor_name' : article_model.contributor_id.username,
                'contributor_companey' : article_model.contributor_id.company if article_model.contributor_id.company != None else self.DEFAULT_USER_COMPANY_NAME,
                }
            article_list.append(article_content)
        
        return article_list
            